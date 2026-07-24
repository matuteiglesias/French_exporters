"""Regression tests for the deterministic v0.2 variance-scaling construction."""

import numpy as np
import pytest

from aggregation_lab import check_scaling_identity
from research.demos.variance_scaling_identity_demo import (
    ATOL,
    RTOL,
    RHO,
    build_analytic_accounting,
    checks_from_contract,
    component_interval_summary,
    interval_summary,
    path_summary,
    scenario_metadata,
)


def contract_outputs():
    components, variance = build_analytic_accounting()
    scaling_components, scaling = check_scaling_identity(components, variance, rtol=RTOL, atol=ATOL)
    paths = path_summary(components, variance)
    intervals = interval_summary(scaling, paths)
    component_intervals = component_interval_summary(scaling_components, intervals, components)
    return paths, intervals, component_intervals, checks_from_contract(paths, intervals)


def test_correlated_equal_weight_alpha_matches_specified_sequence():
    _, intervals, _, _ = contract_outputs()
    correlated = intervals.query("scenario_id == 'scenario_1_rho_0_15'")
    assert correlated["concentration_alpha"].to_numpy() == pytest.approx([1.0] * 4)
    assert correlated["direct_alpha"].to_numpy() == pytest.approx(
        [0.500429, 0.335184, 0.202189, 0.112820], abs=5e-7
    )


def test_component_contract_uses_scientific_identifiers_and_signed_covariance():
    _, _, component_intervals, _ = contract_outputs()
    correlated = component_intervals.query("scenario_id == 'scenario_1_rho_0_15'")
    covariance = correlated.query("component_id == 'B_TOTAL'")
    assert covariance["component_label"].eq("Total doubled covariance").all()
    assert covariance["multiplier"].eq(2.0).all()
    assert (covariance["alpha_contribution"] < 0).all()
    heterogeneous = component_intervals.query("scenario_id == 'scenario_2_heterogeneous_independent'")
    assert set(heterogeneous["component_id"]) == {"A_FAST", "A_SLOW", "B_ZERO"}
    assert heterogeneous.query("component_id == 'B_ZERO'")["numerical_zero"].all()


def test_path_contract_matches_equal_weight_variance_formulas():
    paths, _, _, _ = contract_outputs()
    iid = paths.query("scenario_id == 'scenario_1_iid'")
    correlated = paths.query("scenario_id == 'scenario_1_rho_0_15'")
    assert iid["direct_variance"].to_numpy() == pytest.approx(1 / iid["N"].to_numpy())
    assert correlated["direct_variance"].to_numpy() == pytest.approx(
        RHO + (1 - RHO) / correlated["N"].to_numpy()
    )
    assert correlated["concentration_H"].to_numpy() == pytest.approx(1 / correlated["N"].to_numpy())


def test_metadata_and_scale_aware_checks_follow_contract():
    _, _, _, checks = contract_outputs()
    metadata = scenario_metadata()
    assert set(metadata["scenario_id"]) == {"scenario_1_iid", "scenario_1_rho_0_15", "scenario_2_heterogeneous_independent"}
    assert (checks["allowed_error"] == checks["atol"] + checks["rtol"] * np.maximum(checks["actual"].abs(), checks["expected"].abs())).all()
    assert checks["normalized_error"].le(1).all()
    assert checks["status"].eq("PASS").all()
