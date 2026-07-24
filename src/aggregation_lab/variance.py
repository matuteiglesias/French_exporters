"""Exact accounting of aggregate variance from a contribution panel."""

import numpy as np
import pandas as pd

from .checks import require_close

_KEY_COLUMNS = ["scenario_id", "N", "time", "part"]
_REQUIRED_COLUMNS = _KEY_COLUMNS + ["contribution"]
_GROUP_COLUMNS = ["scenario_id", "N"]
_COMPONENT_COLUMNS = [
    "scenario_id", "N", "left_part", "right_part", "term_type", "covariance",
    "multiplier", "variance_term", "n_observations", "ddof",
]
_SUMMARY_COLUMNS = [
    "scenario_id", "N", "direct_variance", "reconstructed_variance", "residual",
    "n_observations", "ddof",
]


def _part_key(value):
    return (type(value).__name__, repr(value))


def _validate_panel(panel, ddof):
    if not isinstance(panel, pd.DataFrame):
        raise TypeError("panel must be a pandas DataFrame")
    missing = set(_REQUIRED_COLUMNS).difference(panel.columns)
    if missing:
        raise ValueError(f"panel is missing required columns: {sorted(missing)}")
    if not isinstance(ddof, (int, np.integer)) or ddof < 0:
        raise ValueError("ddof must be a nonnegative integer")
    frame = panel.loc[:, _REQUIRED_COLUMNS].copy()
    if frame[_KEY_COLUMNS].isna().any().any():
        raise ValueError("scenario_id, N, time, and part must not be missing")
    if frame.duplicated(_KEY_COLUMNS).any():
        raise ValueError("panel contains duplicate scenario_id, N, time, part rows")
    try:
        frame["N"] = pd.to_numeric(frame["N"], errors="raise")
        frame["contribution"] = pd.to_numeric(frame["contribution"], errors="raise")
    except (TypeError, ValueError) as error:
        raise ValueError("N and contribution must be numeric") from error
    if not np.isfinite(frame["N"]).all() or (frame["N"] <= 0).any():
        raise ValueError("N must be positive and finite")
    if not np.isfinite(frame["contribution"]).all():
        raise ValueError("contribution must be finite")
    for group_key, group in frame.groupby(_GROUP_COLUMNS, sort=False, dropna=False):
        parts = group["part"].unique()
        times = group["time"].unique()
        if len(group) != len(parts) * len(times):
            raise ValueError(f"unbalanced part-by-time panel for {group_key}")
        counts = group.groupby("time", sort=False)["part"].nunique()
        if not (counts == len(parts)).all():
            raise ValueError(f"unbalanced part-by-time panel for {group_key}")
        if len(times) <= ddof:
            raise ValueError(
                f"ddof ({ddof}) must be less than observations ({len(times)}) for {group_key}"
            )
    return frame


def _sorted_frame(frame, columns):
    return frame.sort_values(columns, kind="mergesort").reset_index(drop=True)


def build_variance_components(panel, *, ddof=1):
    """Return diagonal variance and doubled signed covariance terms by scenario/N."""
    frame = _validate_panel(panel, ddof)
    records = []
    for (scenario_id, population), group in frame.groupby(_GROUP_COLUMNS, sort=False):
        parts = sorted(group["part"].unique(), key=_part_key)
        pivot = group.pivot(index="time", columns="part", values="contribution").reindex(columns=parts)
        values = pivot.to_numpy(dtype=float)
        centered = values - values.mean(axis=0, keepdims=True)
        covariance = centered.T @ centered / (len(pivot) - ddof)
        for left_index, left_part in enumerate(parts):
            for right_index in range(left_index, len(parts)):
                right_part = parts[right_index]
                is_diagonal = left_index == right_index
                multiplier = 1.0 if is_diagonal else 2.0
                term_type = "variance" if is_diagonal else "covariance"
                cov = float(covariance[left_index, right_index])
                records.append({
                    "scenario_id": scenario_id, "N": population, "left_part": left_part,
                    "right_part": right_part, "term_type": term_type, "covariance": cov,
                    "multiplier": multiplier, "variance_term": multiplier * cov,
                    "n_observations": len(pivot), "ddof": ddof,
                })
    result = pd.DataFrame.from_records(records, columns=_COMPONENT_COLUMNS)
    return _sorted_frame(result, ["scenario_id", "N", "left_part", "right_part"])


def check_variance_identity(panel, *, ddof=1, rtol=1e-10, atol=1e-12):
    """Return direct and reconstructed aggregate variances, raising on mismatch."""
    frame = _validate_panel(panel, ddof)
    components = build_variance_components(frame, ddof=ddof)
    records = []
    for (scenario_id, population), group in frame.groupby(_GROUP_COLUMNS, sort=False):
        aggregate = group.groupby("time", sort=False)["contribution"].sum().to_numpy(dtype=float)
        direct = float(np.var(aggregate, ddof=ddof))
        component_group = components[
            (components["scenario_id"] == scenario_id) & (components["N"] == population)
        ]
        reconstructed = float(component_group["variance_term"].sum())
        records.append({
            "scenario_id": scenario_id, "N": population, "direct_variance": direct,
            "reconstructed_variance": reconstructed, "residual": direct - reconstructed,
            "n_observations": len(aggregate), "ddof": ddof,
        })
    result = _sorted_frame(pd.DataFrame.from_records(records, columns=_SUMMARY_COLUMNS), _GROUP_COLUMNS)
    require_close(result["direct_variance"], result["reconstructed_variance"], rtol=rtol, atol=atol,
                  label="direct and reconstructed variances")
    return result
