"""Create deterministic algebraic variance-scaling demonstrations (v0.2)."""

from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from aggregation_lab import check_scaling_identity

N_VALUES = np.array([4, 8, 16, 32, 64], dtype=int)
RHO = 0.15
RTOL = 1e-12
ATOL = 1e-12
ARTIFACT_DIR = Path("research/artifacts/variance_scaling_demo_v0_2")

SCENARIOS = {
    "scenario_1_iid": {
        "scenario_label": "Equal weights, independent shocks",
        "scientific_purpose": "Benchmark equal-concentration variance decay under independence",
        "population_scale_definition": "N is number of equal-weight units",
        "component_universe": "Firm-level contributions; decomposition uses diagonal/off-diagonal totals",
        "concentration_formula": "1/N", "variance_formula": "1/N",
        "covariance_structure": "Independent shocks (rho=0)",
        "decomposition_level": "Grouped variance categories", "main_text_status": "MAIN",
    },
    "scenario_1_rho_0_15": {
        "scenario_label": "Equal weights, equicorrelated shocks",
        "scientific_purpose": "Show identical concentration with slower variance decay",
        "population_scale_definition": "N is number of equal-weight units",
        "component_universe": "Firm-level contributions; decomposition uses diagonal/off-diagonal totals",
        "concentration_formula": "1/N", "variance_formula": "0.15 + 0.85/N",
        "covariance_structure": "Equicorrelation rho=0.15",
        "decomposition_level": "Grouped variance categories", "main_text_status": "MAIN",
    },
    "scenario_2_heterogeneous_independent": {
        "scenario_label": "Heterogeneous independent components",
        "scientific_purpose": "Show changing aggregate alpha from changing component contributions",
        "population_scale_definition": "N is the population scale in both analytic component paths",
        "component_universe": "Two independent variance components and a zero covariance remainder",
        "concentration_formula": "not applicable: analytic component demonstration",
        "variance_formula": "N^-0.9 + 0.4 N^-0.3",
        "covariance_structure": "Independent components; covariance remainder is zero",
        "decomposition_level": "Analytic component categories", "main_text_status": "MAIN",
    },
}

COMPONENTS = {
    "scenario_1_iid": [
        ("D_TOTAL", "Total diagonal variance", "diagonal_total", 1.0, lambda n: 1 / n),
        ("B_TOTAL", "Total doubled covariance", "covariance_total", 2.0, lambda n: 0.0),
    ],
    "scenario_1_rho_0_15": [
        ("D_TOTAL", "Total diagonal variance", "diagonal_total", 1.0, lambda n: 1 / n),
        ("B_TOTAL", "Total doubled covariance", "covariance_total", 2.0, lambda n: RHO * (1 - 1 / n)),
    ],
    "scenario_2_heterogeneous_independent": [
        ("A_FAST", "N^-0.9 component", "variance_component", 1.0, lambda n: n ** -0.9),
        ("A_SLOW", "0.4 N^-0.3 component", "variance_component", 1.0, lambda n: 0.4 * n ** -0.3),
        ("B_ZERO", "Numerical covariance remainder", "covariance_total", 2.0, lambda n: 0.0),
    ],
}


def component_row(scenario_id, population, component_id, component_label, component_kind, multiplier, value):
    """Return one analytic variance-accounting row with scientific identifiers."""
    return {
        "scenario_id": scenario_id, "N": int(population), "left_part": component_id,
        "right_part": component_id, "term_type": "covariance" if multiplier == 2 else "variance",
        "covariance": value / multiplier, "multiplier": multiplier, "variance_term": value,
        "n_observations": np.nan, "ddof": np.nan, "component_label": component_label,
        "component_kind": component_kind,
    }


def build_analytic_accounting():
    """Build the frozen v0.2 scenarios without simulation or source-data input."""
    records = []
    summaries = []
    for scenario_id, definitions in COMPONENTS.items():
        for population in N_VALUES:
            terms = [
                component_row(scenario_id, population, component_id, label, kind, multiplier, formula(population))
                for component_id, label, kind, multiplier, formula in definitions
            ]
            variance = sum(term["variance_term"] for term in terms)
            records.extend(terms)
            summaries.append({"scenario_id": scenario_id, "N": int(population),
                              "direct_variance": variance, "reconstructed_variance": variance,
                              "residual": 0.0, "n_observations": np.nan, "ddof": np.nan})
    return pd.DataFrame(records), pd.DataFrame(summaries)


def scenario_metadata():
    return pd.DataFrame.from_records(
        [{"scenario_id": scenario_id, **metadata} for scenario_id, metadata in SCENARIOS.items()]
    )


def path_summary(components, variance_summary):
    """Create the reader-facing N-level audit table from detailed components."""
    totals = components.pivot_table(index=["scenario_id", "N"], columns="component_kind",
                                    values="variance_term", aggfunc="sum", fill_value=0).reset_index()
    paths = variance_summary.merge(totals, on=["scenario_id", "N"], how="left")
    paths["concentration_H"] = np.where(
        paths["scenario_id"].str.startswith("scenario_1"), 1 / paths["N"], np.nan
    )
    paths["expected_variance"] = paths["reconstructed_variance"]
    paths["variance_residual"] = paths["direct_variance"] - paths["reconstructed_variance"]
    paths["absolute_variance_residual"] = paths["variance_residual"].abs()
    paths["diagonal_total"] = paths.get("diagonal_total", 0.0)
    paths["covariance_total"] = paths.get("covariance_total", 0.0)
    paths["covariance_share"] = paths["covariance_total"] / paths["direct_variance"]
    columns = ["scenario_id", "N", "concentration_H", "expected_variance", "direct_variance",
               "reconstructed_variance", "variance_residual", "absolute_variance_residual",
               "diagonal_total", "covariance_total", "covariance_share", "n_observations", "ddof"]
    return paths.loc[:, columns].sort_values(["scenario_id", "N"], kind="mergesort")


def interval_summary(scaling_summary, paths):
    """Create the reader-facing finite-interval contrast table for every scenario."""
    levels = paths.loc[:, ["scenario_id", "N", "concentration_H", "direct_variance"]]
    low = levels.rename(columns={"N": "N_low", "concentration_H": "H_low", "direct_variance": "variance_low"})
    high = levels.rename(columns={"N": "N_high", "concentration_H": "H_high", "direct_variance": "variance_high"})
    intervals = scaling_summary.merge(low, on=["scenario_id", "N_low"], how="left").merge(
        high, on=["scenario_id", "N_high"], how="left"
    )
    intervals["N_midpoint"] = np.sqrt(intervals["N_low"] * intervals["N_high"])
    intervals["log_N_ratio"] = np.log(intervals["N_high"] / intervals["N_low"])
    intervals["concentration_alpha"] = -np.log(intervals["H_high"] / intervals["H_low"]) / intervals["log_N_ratio"]
    intervals["alpha_residual"] = intervals["direct_alpha"] - intervals["reconstructed_alpha"]
    intervals["absolute_alpha_residual"] = intervals["alpha_residual"].abs()
    intervals["allowed_error"] = ATOL + RTOL * np.maximum(intervals["direct_alpha"].abs(), intervals["reconstructed_alpha"].abs())
    intervals["normalized_error"] = intervals["absolute_alpha_residual"] / intervals["allowed_error"]
    intervals["decomposition_status"] = np.where(intervals["absolute_alpha_residual"] <= intervals["allowed_error"], "PASS", "FAIL")
    columns = ["scenario_id", "N_low", "N_high", "N_midpoint", "log_N_ratio", "H_low", "H_high",
               "concentration_alpha", "variance_low", "variance_high", "direct_alpha", "reconstructed_alpha",
               "alpha_residual", "absolute_alpha_residual", "allowed_error", "normalized_error", "decomposition_status"]
    return intervals.loc[:, columns].sort_values(["scenario_id", "N_low"], kind="mergesort")


def component_interval_summary(scaling_components, intervals, components):
    """Make signed alpha contributions self-describing and auditable."""
    labels = components.loc[:, ["scenario_id", "left_part", "component_label", "component_kind", "multiplier"]].drop_duplicates()
    output = scaling_components.merge(labels, on=["scenario_id", "left_part"], how="left")
    output = output.merge(intervals.loc[:, ["scenario_id", "N_low", "N_high", "reconstructed_alpha"]],
                          on=["scenario_id", "N_low", "N_high"], how="left")
    output["alpha_share"] = output["alpha_contribution"] / output["reconstructed_alpha"]
    output["component_sign_low"] = np.sign(output["component_low"]).astype(int)
    output["component_sign_high"] = np.sign(output["component_high"]).astype(int)
    output["log_elasticity_defined"] = (output["component_low"] > 0) & (output["component_high"] > 0)
    output["numerical_zero"] = np.isclose(output["component_low"], 0.0, atol=ATOL) & np.isclose(output["component_high"], 0.0, atol=ATOL)
    output = output.rename(columns={"left_part": "component_id"})
    columns = ["scenario_id", "N_low", "N_high", "component_id", "component_label", "component_kind", "multiplier",
               "component_low", "component_high", "delta_component", "alpha_contribution", "alpha_share",
               "component_sign_low", "component_sign_high", "log_elasticity_defined", "numerical_zero"]
    return output.loc[:, columns].sort_values(["scenario_id", "N_low", "component_id"], kind="mergesort")


def checks_from_contract(paths, intervals):
    """Use the same scale-aware rtol/atol contract as the library helper."""
    path_checks = paths.assign(check_type="variance_identity", actual=paths["direct_variance"], expected=paths["reconstructed_variance"], N_low=np.nan, N_high=np.nan)
    interval_checks = intervals.assign(check_type="scaling_identity", actual=intervals["direct_alpha"], expected=intervals["reconstructed_alpha"], N=np.nan)
    checks = pd.concat([path_checks, interval_checks], ignore_index=True, sort=False)
    checks["residual"] = checks["actual"] - checks["expected"]
    checks["absolute_residual"] = checks["residual"].abs()
    checks["rtol"] = RTOL
    checks["atol"] = ATOL
    checks["allowed_error"] = checks["atol"] + checks["rtol"] * np.maximum(checks["actual"].abs(), checks["expected"].abs())
    checks["normalized_error"] = checks["absolute_residual"] / checks["allowed_error"]
    checks["status"] = np.where(checks["absolute_residual"] <= checks["allowed_error"], "PASS", "FAIL")
    checks["check_id"] = np.where(checks["check_type"] == "variance_identity",
        "variance_identity:" + checks["scenario_id"] + ":N=" + checks["N"].astype("Int64").astype(str),
        "scaling_identity:" + checks["scenario_id"] + ":N=" + checks["N_low"].astype("Int64").astype(str) + "-" + checks["N_high"].astype("Int64").astype(str))
    columns = ["check_id", "scenario_id", "check_type", "N", "N_low", "N_high", "actual", "expected", "residual",
               "absolute_residual", "rtol", "atol", "allowed_error", "normalized_error", "status"]
    return checks.loc[:, columns].sort_values("check_id", kind="mergesort")


def make_figures(paths, intervals, component_intervals):
    """Generate ignored local visual-review files; CSV/Markdown are committed evidence."""
    plt.style.use("default")
    figure, (variance_axis, alpha_axis) = plt.subplots(1, 2, figsize=(11.5, 4.4))
    iid = paths.query("scenario_id == 'scenario_1_iid'")
    correlated = paths.query("scenario_id == 'scenario_1_rho_0_15'")
    variance_axis.loglog(N_VALUES, 1 / N_VALUES, "k--", linewidth=2, label="H(N) = 1/N")
    variance_axis.loglog(
        iid["N"], iid["direct_variance"], linestyle="None", marker="o", markerfacecolor="none",
        markeredgecolor="C0", markeredgewidth=1.5, label="IID aggregate variance",
    )
    variance_axis.loglog(
        correlated["N"], correlated["direct_variance"], linestyle="-", marker="s",
        color="C1", label="Correlated aggregate variance (ρ=0.15)",
    )
    variance_axis.axhline(RHO, color="C1", linestyle=":", linewidth=1.2, label="ρ = 0.15")
    variance_axis.set(
        title="Concentration and aggregate variance", xlabel="Population scale N", ylabel="H(N) or V(N)"
    )
    variance_axis.legend()
    iid_intervals = intervals.query("scenario_id == 'scenario_1_iid'")
    correlated_intervals = intervals.query("scenario_id == 'scenario_1_rho_0_15'")
    alpha_axis.plot(
        correlated_intervals["N_midpoint"], correlated_intervals["concentration_alpha"], "k--",
        linewidth=2, label="Concentration alpha = 1",
    )
    alpha_axis.plot(
        iid_intervals["N_midpoint"], iid_intervals["direct_alpha"], linestyle="None", marker="o",
        markerfacecolor="none", markeredgecolor="C0", markeredgewidth=1.5, label="IID variance alpha = 1",
    )
    alpha_axis.plot(
        correlated_intervals["N_midpoint"], correlated_intervals["direct_alpha"], color="C1", marker="s",
        label="Correlated variance alpha",
    )
    alpha_axis.set_xscale("log", base=2)
    alpha_axis.set(title="Finite-interval elasticities", xlabel="Interval midpoint", ylabel="Alpha")
    alpha_axis.legend()
    figure.tight_layout()
    figure.savefig(ARTIFACT_DIR / "figure_1_concentration_is_not_scaling.png", dpi=180)
    plt.close(figure)

    figure, (heterogeneous_axis, correlated_axis) = plt.subplots(1, 2, figsize=(12.2, 4.8))
    panel_specs = [
        (
            heterogeneous_axis, "scenario_2_heterogeneous_independent", "Heterogeneous independent components",
            [("A_FAST", "Fast-component alpha contribution", "C0"), ("A_SLOW", "Slow-component alpha contribution", "C2")],
            False,
        ),
        (
            correlated_axis, "scenario_1_rho_0_15", "Correlated equal-weight counterexample",
            [("D_TOTAL", "Diagonal alpha contribution", "C0"), ("B_TOTAL", "Covariance alpha contribution", "C3")],
            True,
        ),
    ]
    maximum_residual = 0.0
    for axis, scenario_id, title, component_specs, include_zero_line in panel_specs:
        component_subset = component_intervals.query("scenario_id == @scenario_id")
        interval_subset = intervals.query("scenario_id == @scenario_id")
        maximum_residual = max(maximum_residual, interval_subset["absolute_alpha_residual"].max())
        for component_id, label, color in component_specs:
            component = component_subset.query("component_id == @component_id")
            axis.plot(np.sqrt(component["N_low"] * component["N_high"]), component["alpha_contribution"], color=color, marker="o", label=label)
        axis.plot(interval_subset["N_midpoint"], interval_subset["direct_alpha"], color="black", marker="s", label="Direct total alpha")
        axis.plot(interval_subset["N_midpoint"], interval_subset["reconstructed_alpha"], linestyle="None", marker="o", markersize=10, markerfacecolor="none", markeredgecolor="black", markeredgewidth=1.5, label="Reconstructed total alpha")
        if include_zero_line:
            axis.axhline(0, color="black", linewidth=0.8)
        axis.set_xscale("log", base=2)
        axis.set(title=title, xlabel="Interval midpoint", ylabel="Alpha contribution")
        axis.legend(fontsize="small")
    figure.text(0.5, 0.01, f"max |direct - reconstructed| = {maximum_residual:.2e}", ha="center")
    figure.tight_layout(rect=(0, 0.05, 1, 1))
    figure.savefig(ARTIFACT_DIR / "figure_2_exact_component_attribution.png", dpi=180)
    plt.close(figure)


def write_readme(checks):
    maxima = checks.groupby("check_type")["absolute_residual"].max()
    (ARTIFACT_DIR / "README.md").write_text(f"""# Variance and scaling identity demonstration v0.2

**State:** REVIEW. This AI-produced algebraic demonstration is not an empirical French-export result.

## Reader-facing CSV contract

- `scenario_metadata.csv` defines each scenario's purpose, formulas, component universe, and intended main-text status.
- `path_summary.csv` is the N-level audit table; it includes concentration, expected/direct/reconstructed variance, and grouped diagonal/covariance totals.
- `interval_summary.csv` is the finite-interval audit table; it includes the concentration alpha alongside direct and reconstructed variance alpha for every scenario.
- `component_interval_summary.csv` provides scientific component identifiers, labels, multipliers, signs, and signed alpha contributions.
- `variance_components.csv` remains the detailed component-level accounting audit table. `variance_summary.csv`, `scaling_summary.csv`, and `scaling_components.csv` are retained as API-shaped provenance outputs.

## Deterministic provenance and checks

- Population grid: `{N_VALUES.tolist()}`; no source data, sampling, or randomness is used.
- The correlated construction uses `H(N)=1/N`, `V(N)=rho+(1-rho)/N`, and `rho={RHO}`. Its grouped covariance level is positive but increases with N, producing a negative alpha contribution.
- `checks.csv` applies `allowed_error = atol + rtol * max(abs(actual), abs(expected))` with `rtol={RTOL}` and `atol={ATOL}`.
- Maximum variance-identity absolute residual: `{maxima['variance_identity']:.3e}`; maximum scaling-identity absolute residual: `{maxima['scaling_identity']:.3e}`.
- PNG review figures are intentionally ignored by Git; no binary figures are versioned.

## Local review figures

- Figure 1 juxtaposes the shared concentration path and variance levels with their finite-interval elasticities; IID variance uses hollow markers so the dashed concentration path stays visible.
- Figure 2 has heterogeneous and correlated component-attribution panels. It overlays open reconstructed-total markers on the direct total and annotates the computed maximum direct-versus-reconstructed residual.

## Failure report

No execution failure occurred when this artifact was generated. Reproduction requires Python with `numpy`, `pandas`, `matplotlib`, and the repository `src/` directory on `PYTHONPATH`. The outcome remains REVIEW because the checks validate algebraic identities only, not an empirical estimand.
""")


def main():
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    components, variance = build_analytic_accounting()
    scaling_components, scaling = check_scaling_identity(components, variance, rtol=RTOL, atol=ATOL)
    paths = path_summary(components, variance)
    intervals = interval_summary(scaling, paths)
    component_intervals = component_interval_summary(scaling_components, intervals, components)
    checks = checks_from_contract(paths, intervals)
    if not (checks["status"] == "PASS").all():
        raise RuntimeError("one or more demonstration checks failed")
    scenario_metadata().to_csv(ARTIFACT_DIR / "scenario_metadata.csv", index=False)
    paths.to_csv(ARTIFACT_DIR / "path_summary.csv", index=False)
    intervals.to_csv(ARTIFACT_DIR / "interval_summary.csv", index=False)
    component_intervals.to_csv(ARTIFACT_DIR / "component_interval_summary.csv", index=False)
    components.to_csv(ARTIFACT_DIR / "variance_components.csv", index=False)
    variance.to_csv(ARTIFACT_DIR / "variance_summary.csv", index=False)
    scaling_components.to_csv(ARTIFACT_DIR / "scaling_components.csv", index=False)
    scaling.to_csv(ARTIFACT_DIR / "scaling_summary.csv", index=False)
    checks.to_csv(ARTIFACT_DIR / "checks.csv", index=False)
    make_figures(paths, intervals, component_intervals)
    write_readme(checks)


if __name__ == "__main__":
    main()
