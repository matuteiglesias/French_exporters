"""Create deterministic algebraic demonstrations of aggregation_lab identities."""

from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from aggregation_lab import (
    build_variance_components,
    check_scaling_identity,
    check_variance_identity,
)

N_VALUES = np.array([4, 8, 16, 32, 64], dtype=int)
TIME_COUNT = 256
DDOF = 1
SEED = 20260723
VARIANCE_TOLERANCE = 1e-12
SCALING_TOLERANCE = 1e-10
COVARIANCE_TOLERANCE = 1e-12
ARTIFACT_DIR = Path("research/artifacts/variance_scaling_demo_v0_1")


def exact_identity_basis(time_count, column_count, *, seed, ddof):
    """Return centered columns with exact sample covariance identity."""
    generator = np.random.default_rng(seed)
    raw = generator.normal(size=(time_count, column_count))
    centered = raw - raw.mean(axis=0, keepdims=True)
    orthogonal, _ = np.linalg.qr(centered, mode="reduced")
    return orthogonal[:, :column_count] * np.sqrt(time_count - ddof)


def panel_from_covariance(scenario_id, population, covariance, *, seed):
    """Build an exact finite-sample contribution panel for a target covariance."""
    part_count = covariance.shape[0]
    basis = exact_identity_basis(TIME_COUNT, part_count, seed=seed, ddof=DDOF)
    transformed = basis @ np.linalg.cholesky(covariance).T
    records = [
        {
            "scenario_id": scenario_id,
            "N": int(population),
            "time": time,
            "part": f"part_{part + 1:03d}",
            "contribution": transformed[time, part],
        }
        for time in range(TIME_COUNT)
        for part in range(part_count)
    ]
    return pd.DataFrame.from_records(records), transformed


def scenario_one_covariance(population, rho):
    unit_shock_covariance = (1.0 - rho) * np.eye(population) + rho * np.ones((population, population))
    return unit_shock_covariance / population**2


def scenario_two_covariance(population):
    return np.diag([population ** -0.9, 0.4 * population ** -0.3])


def scenario_three_covariance(population):
    covariance = 0.1 * population ** -0.2
    return np.array([
        [population ** -0.8, covariance],
        [covariance, 0.8 * population ** -0.6],
    ])


def append_scenario(rows, covariance_checks, scenario_id, covariance_function, *, seed_offset):
    for index, population in enumerate(N_VALUES):
        target = covariance_function(int(population))
        if np.any(np.linalg.eigvalsh(target) <= 0):
            raise ValueError(f"target covariance is not positive definite for {scenario_id}, N={population}")
        panel, values = panel_from_covariance(
            scenario_id, population, target, seed=SEED + seed_offset + index
        )
        rows.append(panel)
        measured = np.cov(values, rowvar=False, ddof=DDOF)
        covariance_checks.append({
            "scenario_id": scenario_id,
            "check_type": "designed_covariance",
            "N": int(population),
            "N_low": np.nan,
            "N_high": np.nan,
            "direct_value": float(np.max(np.abs(measured - target))),
            "reconstructed_value": 0.0,
            "residual": float(np.max(np.abs(measured - target))),
            "tolerance": COVARIANCE_TOLERANCE,
            "status": "PASS" if np.max(np.abs(measured - target)) <= COVARIANCE_TOLERANCE else "FAIL",
        })


def make_checks(variance_summary, scaling_summary, covariance_checks):
    checks = list(covariance_checks)
    for row in variance_summary.itertuples(index=False):
        checks.append({
            "scenario_id": row.scenario_id,
            "check_type": "variance_identity",
            "N": row.N,
            "N_low": np.nan,
            "N_high": np.nan,
            "direct_value": row.direct_variance,
            "reconstructed_value": row.reconstructed_variance,
            "residual": row.residual,
            "tolerance": VARIANCE_TOLERANCE,
            "status": "PASS" if abs(row.residual) <= VARIANCE_TOLERANCE else "FAIL",
        })
    for row in scaling_summary.itertuples(index=False):
        checks.append({
            "scenario_id": row.scenario_id,
            "check_type": "scaling_identity",
            "N": np.nan,
            "N_low": row.N_low,
            "N_high": row.N_high,
            "direct_value": row.direct_alpha,
            "reconstructed_value": row.reconstructed_alpha,
            "residual": row.residual,
            "tolerance": SCALING_TOLERANCE,
            "status": "PASS" if abs(row.residual) <= SCALING_TOLERANCE else "FAIL",
        })
    return pd.DataFrame(checks).sort_values(
        ["scenario_id", "check_type", "N", "N_low"], kind="mergesort", na_position="last"
    ).reset_index(drop=True)


def make_figures(variance_summary, scaling_summary, scaling_components):
    plt.style.use("default")
    scenario_one = variance_summary[variance_summary["scenario_id"].isin(["scenario_1_iid", "scenario_1_rho_0_15"])]
    iid = scenario_one[scenario_one["scenario_id"] == "scenario_1_iid"]
    correlated = scenario_one[scenario_one["scenario_id"] == "scenario_1_rho_0_15"]
    figure, axis = plt.subplots(figsize=(7.2, 4.8))
    axis.loglog(N_VALUES, 1 / N_VALUES, "k--", label="H(N) = 1/N")
    axis.loglog(iid["N"], iid["direct_variance"], "o-", label="iid aggregate variance")
    axis.loglog(correlated["N"], correlated["direct_variance"], "s-", label="correlated aggregate variance (rho=0.15)")
    axis.set(title="Equal concentration paths do not imply equal volatility scaling", xlabel="Population N", ylabel="Value")
    axis.legend()
    figure.tight_layout()
    figure.savefig(ARTIFACT_DIR / "figure_1_concentration_is_not_scaling.png", dpi=180)
    plt.close(figure)

    figure, axis = plt.subplots(figsize=(7.2, 4.8))
    for scenario_id, label, marker in [("scenario_2_heterogeneous_independent", "Heterogeneous independent", "o"), ("scenario_3_covariance_adjusted", "Covariance adjusted", "s")]:
        subset = scaling_summary[scaling_summary["scenario_id"] == scenario_id]
        midpoint = np.sqrt(subset["N_low"] * subset["N_high"])
        axis.plot(midpoint, subset["direct_alpha"], marker=marker, linestyle="-", label=f"{label}: direct")
        axis.plot(midpoint, subset["reconstructed_alpha"], marker=marker, linestyle="--", fillstyle="none", label=f"{label}: reconstructed")
    axis.set_xscale("log", base=2)
    axis.set(title="Direct and reconstructed finite-interval alpha", xlabel="Interval midpoint", ylabel="Alpha")
    axis.legend()
    figure.tight_layout()
    figure.savefig(ARTIFACT_DIR / "figure_2_direct_vs_reconstructed_alpha.png", dpi=180)
    plt.close(figure)

    figure, axis = plt.subplots(figsize=(7.2, 4.8))
    subset = scaling_components[scaling_components["scenario_id"] == "scenario_3_covariance_adjusted"].copy()
    subset["midpoint"] = np.sqrt(subset["N_low"] * subset["N_high"])
    labels = {("part_001", "part_001"): "Diagonal A", ("part_002", "part_002"): "Diagonal B", ("part_001", "part_002"): "Signed doubled covariance"}
    for key, label in labels.items():
        component = subset[(subset["left_part"] == key[0]) & (subset["right_part"] == key[1])]
        axis.plot(component["midpoint"], component["alpha_contribution"], marker="o", label=label)
    total = scaling_summary[scaling_summary["scenario_id"] == "scenario_3_covariance_adjusted"]
    axis.plot(np.sqrt(total["N_low"] * total["N_high"]), total["reconstructed_alpha"], "k--", marker="s", label="Reconstructed total alpha")
    axis.axhline(0, color="black", linewidth=0.8)
    axis.set_xscale("log", base=2)
    axis.set(title="Signed alpha contributions from covariance-adjusted components", xlabel="Interval midpoint", ylabel="Alpha contribution")
    axis.legend()
    figure.tight_layout()
    figure.savefig(ARTIFACT_DIR / "figure_3_alpha_component_contributions.png", dpi=180)
    plt.close(figure)


def write_readme(checks):
    maxima = checks.groupby("check_type")["residual"].apply(lambda values: values.abs().max())
    (ARTIFACT_DIR / "README.md").write_text(f"""# Variance and scaling identity demonstration v0.1

## Deterministic provenance

- Population grid: `{N_VALUES.tolist()}`.
- Time observations: `{TIME_COUNT}`.
- `ddof`: `{DDOF}`.
- Random seed: `{SEED}` (with deterministic scenario/population offsets).
- Construction: fixed-seed normal matrices are column-centered, QR-orthogonalized, scaled to exact sample covariance identity under the stated `ddof`, and Cholesky-transformed to each target covariance matrix.

## Scenarios

1. **Same concentration, different volatility.** Equal-weight micro contributions use unit marginal shocks with `rho=0` and `rho=0.15`. `H(N)=1/N`; aggregate variance is `rho + (1-rho)/N`.
2. **Heterogeneous independent parts.** `A1(N)=N^-0.9`, `A2(N)=0.4 N^-0.3`, and `B12(N)=0`.
3. **Covariance-adjusted parts.** `A1(N)=N^-0.8`, `A2(N)=0.8 N^-0.6`, and `B12(N)=0.1 N^-0.2`. Every target covariance matrix was numerically verified positive definite on the stated grid before panel construction.

## Outputs and checks

- `variance_summary.csv` and `variance_components.csv` are produced by the public variance-accounting API.
- `scaling_summary.csv` and `scaling_components.csv` are produced by the public scaling-decomposition API.
- `checks.csv` records designed-versus-measured covariance, variance identity, and scaling identity checks.
- Maximum designed covariance residual: `{maxima['designed_covariance']:.3e}`.
- Maximum variance identity residual: `{maxima['variance_identity']:.3e}`.
- Maximum scaling identity residual: `{maxima['scaling_identity']:.3e}`.
- Figure 1 compares the shared concentration path with iid and correlated aggregate variance paths.
- Figure 2 compares direct and reconstructed alpha for Scenarios 2 and 3.
- Figure 3 shows Scenario 3 diagonal and signed covariance alpha contributions plus their reconstructed total.

## Scientific claim boundary

These are deterministic algebraic demonstrations, not empirical French-export results. They do not validate the reported export alpha. They establish only that the computational chain can represent the intended formal argument: equal concentration paths need not imply equal aggregate-volatility scaling, and signed covariance terms can alter aggregate scaling.
""")


def main():
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    panels = []
    covariance_checks = []
    append_scenario(panels, covariance_checks, "scenario_1_iid", lambda n: scenario_one_covariance(n, 0.0), seed_offset=100)
    append_scenario(panels, covariance_checks, "scenario_1_rho_0_15", lambda n: scenario_one_covariance(n, 0.15), seed_offset=200)
    append_scenario(panels, covariance_checks, "scenario_2_heterogeneous_independent", scenario_two_covariance, seed_offset=300)
    append_scenario(panels, covariance_checks, "scenario_3_covariance_adjusted", scenario_three_covariance, seed_offset=400)
    panel = pd.concat(panels, ignore_index=True)
    variance_components = build_variance_components(panel, ddof=DDOF)
    variance_summary = check_variance_identity(panel, ddof=DDOF, rtol=VARIANCE_TOLERANCE, atol=VARIANCE_TOLERANCE)
    scaling_scenarios = ["scenario_2_heterogeneous_independent", "scenario_3_covariance_adjusted"]
    scaling_components, scaling_summary = check_scaling_identity(
        variance_components[variance_components["scenario_id"].isin(scaling_scenarios)],
        variance_summary[variance_summary["scenario_id"].isin(scaling_scenarios)],
        rtol=SCALING_TOLERANCE,
        atol=SCALING_TOLERANCE,
    )
    checks = make_checks(variance_summary, scaling_summary, covariance_checks)
    if not (checks["status"] == "PASS").all():
        raise RuntimeError("one or more demonstration checks failed")
    variance_summary.to_csv(ARTIFACT_DIR / "variance_summary.csv", index=False)
    variance_components.to_csv(ARTIFACT_DIR / "variance_components.csv", index=False)
    scaling_summary.to_csv(ARTIFACT_DIR / "scaling_summary.csv", index=False)
    scaling_components.to_csv(ARTIFACT_DIR / "scaling_components.csv", index=False)
    checks.to_csv(ARTIFACT_DIR / "checks.csv", index=False)
    make_figures(variance_summary, scaling_summary, scaling_components)
    write_readme(checks)


if __name__ == "__main__":
    main()
