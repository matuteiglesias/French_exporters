# Export Alpha Research Hour Close v0.1

**State:** REVIEW  
**Date:** 2026-07-23  
**Programme:** Economics of Aggregation, Scale, and Measurement  
**Active front:** P2 — Concentration Is Not the Scaling Exponent  
**Stop condition:** reached. No original data opened, no notebook executed, no refactor begun, and no paper architecture expanded.

# RESEARCH HOUR CLOSE

The hour produced a consolidated formal and evidentiary map of the export-alpha argument. It explicitly distinguishes:

- the alpha of a well-defined bin or subpopulation;
- the effective alpha of the whole population;
- variance from standard deviation;
- concentration levels from scaling elasticities;
- diagonal variance contributions from cross-part covariance contributions;
- exact common-alpha inheritance from heterogeneous, scale-dependent aggregation.

The thesis–experiment–figure–code chain is materially clearer, but three provenance breaks remain decisive: the exact producer of the `exp_var_*` families, the final empirical export-alpha estimator, and the common-\(N\) panel needed for direct-versus-reconstructed alpha.

# PI CLARIFICATION

The PI’s remembered interpretation is retained separately from documentary evidence.

The reconstructed interpretation is:

> Each economically coherent population segment can have a local variance-decay exponent determined by its population, micro-moment amplitude, concentration path, and dependence structure. The whole-population exponent is implied by how all segment variance contributions and cross-segment covariance contributions change as total population changes.

This interpretation is compatible with the thesis, but the heterogeneous-alpha aggregation formula is a derived completion in REVIEW rather than a claim that the thesis already stated it explicitly.

# FORMAL RESULT

Let aggregate log-variance be

\[
V_X(N)
=
\sum_q A_q(N)
+
2\sum_{q<r}B_{qr}(N),
\]

where

\[
A_q(N)=\omega_q(N)^2\sigma_q^2(N)
\]

and

\[
B_{qr}(N)
=
\omega_q(N)\omega_r(N)\sigma_{qr}(N).
\]

Define

\[
\alpha_{\mathrm{eff}}(N)
=
-\frac{d\log V_X(N)}{d\log N}.
\]

Then the exact local decomposition is

\[
\boxed{
\alpha_{\mathrm{eff}}(N)
=
\sum_q
\frac{A_q(N)}{V_X(N)}a_q(N)
+
2\sum_{q<r}
\frac{B_{qr}(N)}{V_X(N)}b_{qr}(N)
}
\]

with

\[
a_q=-\frac{d\log A_q}{d\log N},
\]

and the signed definition

\[
b_{qr}B_{qr}
=
-\frac{dB_{qr}}{d\log N}.
\]

If part weights are fixed, \(n_q=c_qN\), cross covariance is negligible, and

\[
\sigma_q^2=K_qn_q^{-\alpha_q},
\]

then

\[
\alpha_{\mathrm{eff}}(N)
=
\sum_q
\pi_q(N)\alpha_q,
\qquad
\pi_q(N)
=
\frac{\omega_q^2\sigma_q^2(N)}
{\sum_j\omega_j^2\sigma_j^2(N)}.
\]

This is a local variance-contribution-weighted elasticity, not generally a fixed weighted average.

# CONDITIONS FOR AGGREGATING SUBPOPULATION ALPHAS

A conventional weighted-average description requires:

1. a fixed and comparable partition across population sizes;
2. proportional part growth \(n_q=c_qN\);
3. stable part value shares;
4. the same variance object in every part and in the total;
5. stable micro moments and within-part dependence laws;
6. negligible or separately modeled cross-part covariance;
7. locally power-law part contributions;
8. a stated population-size range.

If all part alphas are equal, the common exponent is inherited exactly.

If part alphas differ but covariance is negligible, the result is a scale-dependent contribution-weighted combination.

If covariance matters, the result is covariance-adjusted and need not lie within the range of part alphas.

If all contributions are positive power laws, the slowest-decaying component dominates asymptotically.

# THESIS → EXPERIMENT → FIGURE → CODE MAP

The supported chain is:

```text
thesis micro-moment formulas
→ power-sum experiments
→ equal-value population groups
→ group variance construction
→ variance-versus-population figures
```

Directly recovered links include:

- `Log of sum of powers.ipynb` for nonlinear shock-family and population-size experiments;
- `Experiment 5. Simple var vs nq, s. (s).ipynb` for group populations and total/noise/base variances;
- `Sigma vs log(n), q plots.ipynb` for `var_diff_qi` versus population and the two `sigma_vs_n_*.png` figures;
- `Experiment 2. Extensive BME.ipynb` for base/total bootstrap panels and covariance matrices.

The unresolved continuation is:

```text
verified exp_var producer
→ fitted local bin alphas
→ common-N covariance elasticities
→ reconstructed aggregate alpha
→ reported empirical export alpha
```

The full row-level map and DIRECT / PLAUSIBLE / INFERRED / MISSING / CONTRADICTED classifications are in `export_alpha_synthesis_map_v0_1.md`.

# STRONGEST SUPPORTED SYNTHESIS

> Heterogeneous subpopulations can have different local variance-decay exponents because their populations, micro moments, concentration paths, and covariance structures differ. A coherent aggregate scaling pattern can nevertheless emerge because aggregate variance is the sum of scale-dependent diagonal and covariance contributions. The whole-population alpha is therefore best interpreted as a covariance-adjusted, contribution-weighted, scale-dependent effective elasticity. It reduces to a common subpopulation alpha under common-exponent assumptions and approximates a variance-contribution-weighted combination of heterogeneous alphas only under restrictive conditions.

This statement remains REVIEW and does not claim novelty or empirical validation.

# CRITIC’S WARNING

The most important hidden assumption is that increasing \(N\) defines a stable population-scaling path.

If the partition, part shares, micro moments, or dependence structure change with \(N\), the fitted alpha mixes diversification with composition and regime change.

The weighted-average intuition fails when a slowly decaying covariance term dominates. For example, diagonal exponents \(0.8\) and \(0.6\) do not imply an aggregate exponent between them if a positive covariance contribution decays as \(N^{-0.2}\).

The intuition becomes approximately valid only with fixed composition, proportional part growth, stable micro laws, negligible covariance, and locally power-law part variances.

The thesis distinguishes these mechanisms qualitatively and partially quantitatively, but it does not yet contain the decisive common-\(N\), direct-versus-reconstructed comparison.

A second warning concerns moment existence: for an ideal unbounded log-Laplace shock, a finite mean does not guarantee a finite variance. Variance-based alpha must identify whether the operative object is theoretical, clipped, truncated, empirical-support, or finite-sample.

# ARTIFACT PRODUCED

Primary artifact:

```text
research/artifacts/export_alpha_synthesis_map_v0_1.md
```

Supporting artifacts:

```text
research/artifacts/export_alpha_formal_framework_compendium_v0_1.md
research/guides/french_exporters_notebook_atlas_v0_1.md
research/artifacts/export_alpha_research_hour_close_v0_1.md
```

All artifacts are in REVIEW.

# NEXT EXECUTABLE TEST

Using existing generated outputs only, construct one common population-size-indexed table containing:

\[
N,\quad
V_X(N),\quad
A_q(N),\quad
B_{qr}(N),\quad
n_q(N).
\]

Compute:

\[
\widehat\alpha_{\mathrm{direct}}(N)
=
-\frac{\Delta\log V_X(N)}
{\Delta\log N},
\]

the diagonal-only reconstruction,

\[
\widehat\alpha_{\mathrm{diagonal}}(N)
=
\sum_q
\frac{A_q(N)}{V_X(N)}
\widehat a_q(N),
\]

and the full reconstruction,

\[
\widehat\alpha_{\mathrm{full}}(N)
=
\widehat\alpha_{\mathrm{diagonal}}(N)
+
2\sum_{q<r}
\frac{B_{qr}(N)}{V_X(N)}
\widehat b_{qr}(N).
\]

Interpretation:

- full succeeds, diagonal fails: covariance is empirically necessary;
- both succeed: covariance is negligible over that range;
- neither succeeds: composition drift, inconsistent estimands, missing components, or no stable scalar alpha.

Pass condition and numerical tolerance must be frozen before execution.

# EXACT RESTART POINTER

Open:

```text
code/notebooks/Experiment 4. Micro shocks. (s, gr, size dists).ipynb
```

Search only for:

```text
exp_var_
to_csv
aggregated_simulation_results
var_diff_qi
var_diff_agg_i
```

Record:

1. every exact output filename;
2. the output schema;
3. definitions of \(N\), `Q`, `q`, `n`, `s`, `i`, `var_diff_qi`, and `var_diff_agg_i`;
4. shock and size-distribution labels;
5. repetition count and random-seed status;
6. which downstream `Sigma vs log(n), q plots.ipynb` load statements each output satisfies.

Stop immediately after confirming or rejecting Experiment 4 as the producer of the `exp_var_*` families. Do not open the original data or execute the notebook.
