"""Finite-interval scaling decomposition for variance components."""

import numpy as np
import pandas as pd

from .checks import require_close

_GROUP_COLUMNS = ["scenario_id"]
_COMPONENT_KEY = ["left_part", "right_part", "term_type"]
_OUTPUT_COMPONENT_COLUMNS = [
    "scenario_id", "N_low", "N_high", "left_part", "right_part", "term_type",
    "component_low", "component_high", "delta_component", "alpha_contribution",
]
_OUTPUT_SUMMARY_COLUMNS = [
    "scenario_id", "N_low", "N_high", "direct_alpha", "reconstructed_alpha",
    "residual", "log_mean_variance",
]


def logarithmic_mean(a, b):
    """Return (a-b)/(log(a)-log(b)) stably for positive finite inputs."""
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    if not np.all(np.isfinite(a)) or not np.all(np.isfinite(b)) or np.any(a <= 0) or np.any(b <= 0):
        raise ValueError("logarithmic mean inputs must be positive and finite")
    log_ratio = np.log(b / a)
    with np.errstate(divide="ignore", invalid="ignore"):
        result = a * np.expm1(log_ratio) / log_ratio
    return np.where(log_ratio == 0.0, a, result)


def _validate_inputs(components, summary, *, rtol, atol):
    needed_components = {"scenario_id", "N", *_COMPONENT_KEY, "variance_term"}
    needed_summary = {"scenario_id", "N", "direct_variance"}
    if not isinstance(components, pd.DataFrame) or not isinstance(summary, pd.DataFrame):
        raise TypeError("components and summary must be pandas DataFrames")
    if missing := needed_components.difference(components.columns):
        raise ValueError(f"components are missing required columns: {sorted(missing)}")
    if missing := needed_summary.difference(summary.columns):
        raise ValueError(f"summary is missing required columns: {sorted(missing)}")
    component_frame = components.copy()
    summary_frame = summary.copy()
    if component_frame.duplicated(["scenario_id", "N", *_COMPONENT_KEY]).any():
        raise ValueError("components contain duplicate scenario/N/component rows")
    if summary_frame.duplicated(["scenario_id", "N"]).any():
        raise ValueError("summary contains duplicate scenario/N rows")
    for frame, columns, label in (
        (component_frame, ["N", "variance_term"], "components"),
        (summary_frame, ["N", "direct_variance"], "summary"),
    ):
        try:
            frame[columns] = frame[columns].apply(pd.to_numeric, errors="raise")
        except (TypeError, ValueError) as error:
            raise ValueError(f"{label} numeric fields must be numeric") from error
    if not np.isfinite(component_frame[["N", "variance_term"]].to_numpy(dtype=float)).all():
        raise ValueError("components N and variance_term must be finite")
    if not np.isfinite(summary_frame[["N", "direct_variance"]].to_numpy(dtype=float)).all():
        raise ValueError("summary N and direct_variance must be finite")
    if (component_frame["N"] <= 0).any() or (summary_frame["N"] <= 0).any():
        raise ValueError("N must be positive and finite")
    if (summary_frame["direct_variance"] <= 0).any():
        raise ValueError("direct_variance must be positive and finite before logarithms")
    component_pairs = set(map(tuple, component_frame[["scenario_id", "N"]].drop_duplicates().to_numpy()))
    summary_pairs = set(map(tuple, summary_frame[["scenario_id", "N"]].drop_duplicates().to_numpy()))
    if component_pairs != summary_pairs:
        raise ValueError("components and summary must cover the same scenario/N values")
    for scenario_id, scenario_summary in summary_frame.groupby("scenario_id", sort=False):
        levels = scenario_summary.sort_values("N", kind="mergesort")["N"].to_list()
        for low, high in zip(levels[:-1], levels[1:]):
            low_keys = set(map(tuple, component_frame.loc[
                (component_frame["scenario_id"] == scenario_id) & (component_frame["N"] == low),
                _COMPONENT_KEY,
            ].to_numpy()))
            high_keys = set(map(tuple, component_frame.loc[
                (component_frame["scenario_id"] == scenario_id) & (component_frame["N"] == high),
                _COMPONENT_KEY,
            ].to_numpy()))
            if low_keys != high_keys:
                raise ValueError(
                    f"component universe differs between adjacent N values {low} and {high} "
                    f"for scenario {scenario_id!r}"
                )
    reconstructed = (
        component_frame.groupby(["scenario_id", "N"], sort=False)["variance_term"]
        .sum()
        .reindex(pd.MultiIndex.from_frame(summary_frame[["scenario_id", "N"]]))
        .to_numpy(dtype=float)
    )
    require_close(
        summary_frame["direct_variance"].to_numpy(dtype=float),
        reconstructed,
        rtol=rtol,
        atol=atol,
        label="summary direct variances and component variance terms",
    )
    return component_frame, summary_frame


def decompose_scaling_intervals(components, summary, *, rtol=1e-10, atol=1e-12):
    """Decompose adjacent-N direct scaling into exact signed component contributions."""
    components, summary = _validate_inputs(components, summary, rtol=rtol, atol=atol)
    component_records = []
    summary_records = []
    for scenario_id, scenario_summary in summary.groupby("scenario_id", sort=False):
        scenario_summary = scenario_summary.sort_values("N", kind="mergesort")
        if scenario_summary["N"].nunique() < 2:
            raise ValueError(f"scenario {scenario_id!r} needs at least two distinct N values")
        levels = scenario_summary["N"].to_list()
        for low, high in zip(levels[:-1], levels[1:]):
            low_components = components[(components["scenario_id"] == scenario_id) & (components["N"] == low)]
            high_components = components[(components["scenario_id"] == scenario_id) & (components["N"] == high)]
            low_keys = set(map(tuple, low_components[_COMPONENT_KEY].to_numpy()))
            high_keys = set(map(tuple, high_components[_COMPONENT_KEY].to_numpy()))
            if low_keys != high_keys:
                raise ValueError(
                    f"component universe differs between adjacent N values {low} and {high} "
                    f"for scenario {scenario_id!r}"
                )
            low_indexed = low_components.set_index(_COMPONENT_KEY)["variance_term"]
            high_indexed = high_components.set_index(_COMPONENT_KEY)["variance_term"]
            low_variance = float(scenario_summary.loc[scenario_summary["N"] == low, "direct_variance"].iloc[0])
            high_variance = float(scenario_summary.loc[scenario_summary["N"] == high, "direct_variance"].iloc[0])
            log_n = float(np.log(high) - np.log(low))
            log_mean = float(logarithmic_mean(low_variance, high_variance))
            direct_alpha = -float(np.log(high_variance) - np.log(low_variance)) / log_n
            contributions = []
            for key in sorted(low_keys, key=lambda item: tuple(map(repr, item))):
                low_value = float(low_indexed.loc[key])
                high_value = float(high_indexed.loc[key])
                alpha = -(high_value - low_value) / (log_mean * log_n)
                contributions.append(alpha)
                component_records.append({
                    "scenario_id": scenario_id, "N_low": low, "N_high": high,
                    "left_part": key[0], "right_part": key[1], "term_type": key[2],
                    "component_low": low_value, "component_high": high_value,
                    "delta_component": high_value - low_value, "alpha_contribution": alpha,
                })
            reconstructed = float(np.sum(contributions))
            summary_records.append({
                "scenario_id": scenario_id, "N_low": low, "N_high": high,
                "direct_alpha": direct_alpha, "reconstructed_alpha": reconstructed,
                "residual": direct_alpha - reconstructed, "log_mean_variance": log_mean,
            })
    component_output = pd.DataFrame.from_records(component_records, columns=_OUTPUT_COMPONENT_COLUMNS)
    summary_output = pd.DataFrame.from_records(summary_records, columns=_OUTPUT_SUMMARY_COLUMNS)
    component_output = component_output.sort_values(
        ["scenario_id", "N_low", "N_high", "left_part", "right_part"], kind="mergesort"
    ).reset_index(drop=True)
    summary_output = summary_output.sort_values(["scenario_id", "N_low", "N_high"], kind="mergesort").reset_index(drop=True)
    return component_output, summary_output


def check_scaling_identity(components, summary, *, rtol=1e-10, atol=1e-12):
    """Return scaling decomposition outputs, raising if finite-interval identity fails."""
    component_output, summary_output = decompose_scaling_intervals(components, summary, rtol=rtol, atol=atol)
    require_close(summary_output["direct_alpha"], summary_output["reconstructed_alpha"], rtol=rtol, atol=atol,
                  label="direct and reconstructed scaling exponents")
    return component_output, summary_output
