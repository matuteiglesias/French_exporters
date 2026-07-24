# Variance and scaling identity demonstration v0.2

**State:** REVIEW. This AI-produced algebraic demonstration is not an empirical French-export result.

## Reader-facing CSV contract

- `scenario_metadata.csv` defines each scenario's purpose, formulas, component universe, and intended main-text status.
- `path_summary.csv` is the N-level audit table; it includes concentration, expected/direct/reconstructed variance, and grouped diagonal/covariance totals.
- `interval_summary.csv` is the finite-interval audit table; it includes the concentration alpha alongside direct and reconstructed variance alpha for every scenario.
- `component_interval_summary.csv` provides scientific component identifiers, labels, multipliers, signs, and signed alpha contributions.
- `variance_components.csv` remains the detailed component-level accounting audit table. `variance_summary.csv`, `scaling_summary.csv`, and `scaling_components.csv` are retained as API-shaped provenance outputs.

## Deterministic provenance and checks

- Population grid: `[4, 8, 16, 32, 64]`; no source data, sampling, or randomness is used.
- The correlated construction uses `H(N)=1/N`, `V(N)=rho+(1-rho)/N`, and `rho=0.15`. Its grouped covariance level is positive but increases with N, producing a negative alpha contribution.
- `checks.csv` applies `allowed_error = atol + rtol * max(abs(actual), abs(expected))` with `rtol=1e-12` and `atol=1e-12`.
- Maximum variance-identity absolute residual: `0.000e+00`; maximum scaling-identity absolute residual: `6.661e-16`.
- PNG review figures are intentionally ignored by Git; no binary figures are versioned.

## Local review figures

- Figure 1 juxtaposes the shared concentration path and variance levels with their finite-interval elasticities; IID variance uses hollow markers so the dashed concentration path stays visible.
- Figure 2 has heterogeneous and correlated component-attribution panels. It overlays open reconstructed-total markers on the direct total and annotates the computed maximum direct-versus-reconstructed residual.

## Failure report

No execution failure occurred when this artifact was generated. Reproduction requires Python with `numpy`, `pandas`, `matplotlib`, and the repository `src/` directory on `PYTHONPATH`. The outcome remains REVIEW because the checks validate algebraic identities only, not an empirical estimand.
