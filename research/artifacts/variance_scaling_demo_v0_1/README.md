# Variance and scaling identity demonstration v0.1

## Deterministic provenance

- Population grid: `[4, 8, 16, 32, 64]`.
- Time observations: `256`.
- `ddof`: `1`.
- Random seed: `20260723` (with deterministic scenario/population offsets).
- Construction: fixed-seed normal matrices are column-centered, QR-orthogonalized, scaled to exact sample covariance identity under the stated `ddof`, and Cholesky-transformed to each target covariance matrix.

## Scenarios

1. **Same concentration, different volatility.** Equal-weight micro contributions use unit marginal shocks with `rho=0` and `rho=0.15`. `H(N)=1/N`; aggregate variance is `rho + (1-rho)/N`.
2. **Heterogeneous independent parts.** `A1(N)=N^-0.9`, `A2(N)=0.4 N^-0.3`, and `B12(N)=0`.
3. **Covariance-adjusted parts.** `A1(N)=N^-0.8`, `A2(N)=0.8 N^-0.6`, and `B12(N)=0.1 N^-0.2`. Every target covariance matrix was numerically verified positive definite on the stated grid before panel construction.

## Outputs and checks

- `variance_summary.csv` and `variance_components.csv` are produced by the public variance-accounting API.
- `scaling_summary.csv` and `scaling_components.csv` are produced by the public scaling-decomposition API.
- `checks.csv` records designed-versus-measured covariance, variance identity, and scaling identity checks.
- Maximum designed covariance residual: `2.776e-16`.
- Maximum variance identity residual: `1.665e-16`.
- Maximum scaling identity residual: `5.551e-16`.
- Figure 1 compares the shared concentration path with iid and correlated aggregate variance paths.
- Figure 2 compares direct and reconstructed alpha for Scenarios 2 and 3.
- Figure 3 shows Scenario 3 diagonal and signed covariance alpha contributions plus their reconstructed total.

## Scientific claim boundary

These are deterministic algebraic demonstrations, not empirical French-export results. They do not validate the reported export alpha. They establish only that the computational chain can represent the intended formal argument: equal concentration paths need not imply equal aggregate-volatility scaling, and signed covariance terms can alter aggregate scaling.
