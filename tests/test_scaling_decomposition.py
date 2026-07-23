import numpy as np
import pandas as pd
import pytest

from aggregation_lab.scaling import check_scaling_identity, decompose_scaling_intervals, logarithmic_mean
from aggregation_lab.variance import build_variance_components, check_variance_identity


def panel_for_levels():
    rows = []
    for n, a, b in [(1, [0, 2, 1, 3], [3, 1, 2, 2]), (2, [0, 1, 0.5, 1.5], [1.5, 0.5, 1, 0.5])]:
        for part, values in {"a": a, "b": b}.items():
            rows.extend({"scenario_id": "s", "N": n, "time": t, "part": part, "contribution": x}
                        for t, x in enumerate(values))
    return pd.DataFrame(rows)


def accounting_inputs():
    frame = panel_for_levels()
    return build_variance_components(frame), check_variance_identity(frame)


def test_direct_and_reconstructed_scaling_are_equal():
    components, summary = accounting_inputs()
    _, scaling = check_scaling_identity(components, summary)
    assert scaling.loc[0, "residual"] == pytest.approx(0, abs=1e-12)


def test_signed_covariance_contribution_is_preserved():
    components, summary = accounting_inputs()
    scaling_components, _ = check_scaling_identity(components, summary)
    covariance = scaling_components.query("term_type == 'covariance'").iloc[0]
    assert covariance["alpha_contribution"] != 0


def test_equal_aggregate_variance_has_zero_direct_alpha():
    components = pd.DataFrame([
        {"scenario_id": "s", "N": n, "left_part": "a", "right_part": "a", "term_type": "variance", "variance_term": 2.0}
        for n in [1, 2]
    ])
    summary = pd.DataFrame([{"scenario_id": "s", "N": n, "direct_variance": 2.0} for n in [1, 2]])
    _, output = check_scaling_identity(components, summary)
    assert output.loc[0, "direct_alpha"] == pytest.approx(0)
    assert output.loc[0, "reconstructed_alpha"] == pytest.approx(0)


def test_inconsistent_component_and_direct_variances_are_rejected():
    components, summary = accounting_inputs()
    components.loc[components["N"] == 1, "variance_term"] += 1.0
    with pytest.raises(ValueError, match="component variance terms"):
        decompose_scaling_intervals(components, summary)


def test_component_universe_mismatch_is_rejected():
    components, summary = accounting_inputs()
    components = components[~((components["N"] == 2) & (components["term_type"] == "covariance"))]
    with pytest.raises(ValueError, match="component universe differs"):
        decompose_scaling_intervals(components, summary)


def test_nonpositive_variance_is_rejected_before_logarithm():
    components, summary = accounting_inputs()
    summary.loc[summary["N"] == 2, "direct_variance"] = 0
    with pytest.raises(ValueError, match="positive and finite"):
        decompose_scaling_intervals(components, summary)


def test_logarithmic_mean_is_stable_for_equal_and_nearly_equal_inputs():
    assert logarithmic_mean(3.0, 3.0) == pytest.approx(3.0)
    near = logarithmic_mean(1.0, np.nextafter(1.0, 2.0))
    assert near == pytest.approx(1.0, rel=1e-14)


def test_scaling_output_is_invariant_to_component_input_order():
    components, summary = accounting_inputs()
    first = decompose_scaling_intervals(components, summary)
    second = decompose_scaling_intervals(
        components.sample(frac=1, random_state=9), summary.sample(frac=1, random_state=10)
    )
    pd.testing.assert_frame_equal(first[0], second[0])
    pd.testing.assert_frame_equal(first[1], second[1])
