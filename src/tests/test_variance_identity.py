import numpy as np
import pandas as pd
import pytest

from aggregation_lab.checks import require_close
from aggregation_lab.variance import build_variance_components, check_variance_identity


def panel(values, *, n=1, scenario="s"):
    return pd.DataFrame([
        {"scenario_id": scenario, "N": n, "time": time, "part": part, "contribution": value}
        for part, series in values.items() for time, value in enumerate(series)
    ])


def test_exact_two_part_variance_identity():
    frame = panel({"a": [1, 2, 3], "b": [2, 1, 0]})
    summary = check_variance_identity(frame)
    assert summary.loc[0, "direct_variance"] == pytest.approx(0.0)
    assert summary.loc[0, "residual"] == pytest.approx(0.0, abs=1e-12)


def test_negative_covariance_is_preserved_and_doubled_once():
    components = build_variance_components(panel({"a": [0, 1, 2], "b": [2, 1, 0]}))
    covariance = components.query("term_type == 'covariance'").iloc[0]
    assert covariance["covariance"] < 0
    assert covariance["multiplier"] == 2
    assert covariance["variance_term"] == pytest.approx(2 * covariance["covariance"])


def test_three_part_variance_identity():
    summary = check_variance_identity(panel({"a": [1, 2, 4, 8], "b": [0, 1, 0, 1], "c": [2, 0, 3, 1]}))
    assert summary.loc[0, "residual"] == pytest.approx(0, abs=1e-12)


def test_duplicate_row_is_rejected():
    frame = panel({"a": [1, 2], "b": [3, 4]})
    with pytest.raises(ValueError, match="duplicate"):
        build_variance_components(pd.concat([frame, frame.iloc[[0]]], ignore_index=True))


def test_missing_part_time_observation_is_rejected():
    frame = panel({"a": [1, 2], "b": [3, 4]}).drop(index=3)
    with pytest.raises(ValueError, match="unbalanced"):
        build_variance_components(frame)


@pytest.mark.parametrize("bad_n", [0, -1, np.inf])
def test_invalid_or_nonpositive_n_is_rejected(bad_n):
    with pytest.raises(ValueError, match="positive and finite"):
        build_variance_components(panel({"a": [1, 2]}, n=bad_n))


def test_ddof_must_be_less_than_observations():
    with pytest.raises(ValueError, match="ddof"):
        build_variance_components(panel({"a": [1, 2]}), ddof=2)


def test_output_is_invariant_to_input_row_order():
    frame = panel({"b": [1, 2, 4], "a": [3, 1, 2]}, n=2)
    pd.testing.assert_frame_equal(
        build_variance_components(frame),
        build_variance_components(frame.sample(frac=1, random_state=7)),
    )


def test_scale_aware_tolerance_accepts_large_scale_roundoff_and_rejects_material_error():
    require_close([1e12], [1e12 + 10], rtol=1e-10, atol=1e-12)
    with pytest.raises(ValueError, match="differ"):
        require_close([1e-8], [2e-8], rtol=1e-10, atol=1e-12)
