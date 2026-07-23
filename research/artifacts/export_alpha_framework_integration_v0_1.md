# Export Alpha Framework Integration v0.1

**State:** REVIEW  
**Date:** 2026-07-23  
**Programme:** Economics of Aggregation, Scale, and Measurement  
**Active front:** P2 — Concentration Is Not the Scaling Exponent

## Purpose

Integrate the completed PI research hour into durable laboratory state and distinguish the new formal contribution from thesis-backed results, code evidence, and untested empirical claims.

## PI-directed scientific clarification

There is not necessarily one uniquely authoritative scalar alpha that should be estimated independently of population segment and scale. Economically coherent subpopulations may have different local variance-decay exponents because their population sizes, micro moments, concentration paths, and dependence structures differ.

The whole-population exponent should therefore be treated provisionally as an effective elasticity implied by all diagonal variance and covariance contributions as total population changes.

This is an accepted PI research direction. The mathematical completion and empirical interpretation remain in REVIEW until validated.

## Formal object

Let

\[
V_X(N)=\sum_q A_q(N)+2\sum_{q<r}B_{qr}(N),
\]

with

\[
A_q(N)=\omega_q(N)^2\sigma_q^2(N)
\]

and

\[
B_{qr}(N)=\omega_q(N)\omega_r(N)\sigma_{qr}(N).
\]

Define

\[
\alpha_{\mathrm{eff}}(N)
=-\frac{d\log V_X(N)}{d\log N}.
\]

The candidate local decomposition is

\[
\alpha_{\mathrm{eff}}(N)
=
\sum_q\frac{A_q(N)}{V_X(N)}a_q(N)
+
2\sum_{q<r}\frac{B_{qr}(N)}{V_X(N)}b_{qr}(N),
\]

where

\[
a_q=-\frac{d\log A_q}{d\log N}
\]

and signed covariance contributions are defined by

\[
b_{qr}B_{qr}=-\frac{dB_{qr}}{d\log N}.
\]

When part weights are fixed, part populations grow proportionally, and cross-part covariance is negligible, this reduces locally to a variance-contribution-weighted combination of part alphas. It is not generally a fixed arithmetic average.

## Evidence classification

### PI accepted direction

- distinguish local bin alphas from the effective whole-population alpha;
- treat concentration as a level and alpha as a scaling elasticity;
- retain covariance terms rather than assuming a covariance-free average;
- pursue a direct-versus-reconstructed alpha test as the central empirical adjudication.

### Thesis-backed or directly supported

- the thesis defines population scaling of part variances and derives common-alpha inheritance under common-exponent assumptions;
- nonlinear micro moments affect aggregate variance amplitudes;
- within-part comovement can delay ordinary `1/n` variance decay;
- existing notebooks construct equal-value groups, simulate shocks, calculate group variances, plot variance against population, and generate covariance outputs.

### Derived completion in REVIEW

- heterogeneous part alphas imply a scale-dependent contribution-weighted elasticity when covariance is negligible;
- the complete aggregate expression requires signed covariance-elasticity contributions;
- the slowest-decaying positive contribution dominates asymptotically under positive power-law components;
- a fitted finite-range alpha may be a secant approximation to a scale-dependent local elasticity.

### Not yet demonstrated

- that the reported export coefficient is reproduced by the recovered code;
- that cross-bin covariance is negligible or necessary over the tested range;
- that a stable population-scaling path preserves partition definitions, shares, moments, and dependence;
- that direct and reconstructed alpha agree on a common `N` grid;
- that the formal completion is novel relative to the literature.

## Current provenance chain

Materially supported:

```text
thesis micro-moment formulas
→ power-sum experiments
→ equal-value group construction
→ simulated or empirical group variances
→ variance-versus-population figures
```

Still incomplete:

```text
verified exp_var producer
→ fitted local bin alphas
→ common-N covariance elasticities
→ reconstructed aggregate alpha
→ reported empirical export alpha
```

The three decisive missing links are:

1. exact producer and schema of the `exp_var_*` families;
2. final empirical export-alpha estimator, including sign and variance convention;
3. common-`N` variance-accounting panel containing total, diagonal, covariance, and population terms.

## Central falsifiable test

Construct, from existing generated outputs where possible, one common population-size-indexed panel containing

\[
N,\quad V_X(N),\quad A_q(N),\quad B_{qr}(N),\quad n_q(N).
\]

Compare:

1. direct local elasticity;
2. diagonal-only reconstruction;
3. full covariance-adjusted reconstruction.

Interpretation:

- full succeeds and diagonal fails: covariance is empirically necessary;
- both succeed: covariance is negligible over the tested range;
- neither succeeds: the estimands are inconsistent, components are missing, composition changes, or no stable scalar alpha exists.

The numerical tolerance and exact estimands must be frozen before execution.

## Publication trajectory

### Gate 0 — Formal recovery

**Status:** achieved in REVIEW.

A coherent mathematical and evidentiary account now exists. It does not yet constitute a validated paper result.

### Gate 1 — Lineage closure

Verify the producers, schemas, consumers, filters, seeds, and durable outputs for the principal simulation and empirical families.

### Gate 2 — Estimand and test freeze

Freeze:

- positive alpha versus signed slope;
- variance object;
- population path;
- partition invariance;
- moment/truncation convention;
- covariance treatment;
- finite population range;
- validation tolerance.

### Gate 3 — Direct reproduction

Reproduce the empirical export-alpha coefficient with source data, exact code, output, uncertainty, and sign convention.

### Gate 4 — Micro-to-macro reconstruction

Build the common-`N` panel and perform direct, diagonal-only, and full reconstruction comparisons.

### Gate 5 — Adversarial validation

Only after the central reconstruction runs:

- population-range sensitivity;
- sorted versus random partitions;
- alternative bin counts;
- moment-existence and truncation checks;
- log-level versus linear-level mapping;
- seed and Monte Carlo stability;
- export/import comparison where scientifically justified.

### Gate 6 — Claim and novelty freeze

Run a targeted literature review against the validated mechanism and accepted empirical result. Decide whether the paper is primarily:

- a correction to concentration-based granularity interpretations;
- a constructive nonlinear micro-to-macro aggregation framework;
- an empirical covariance decomposition of trade volatility;
- or a tightly integrated version of these contributions.

No novelty claim should be made before this gate.

### Gate 7 — Paper and replication package

Only after claim freeze:

- create the paper architecture;
- extract minimal clean modules from legacy notebooks;
- produce final figures and tables from scripted entry points;
- document data provenance and confidential-data boundaries;
- build a public or controlled replication package;
- select venue and prepare submission.

## Working paper nucleus

The current strongest provisional nucleus is:

> Concentration is a state variable, while the variance-decay exponent is a scale-dependent elasticity of all variance and covariance contributions. Heterogeneous local alphas can combine coherently at the aggregate level, but generally through contribution weights and covariance corrections rather than a fixed average.

This is a REVIEW framing, not a novelty, causal, or publication claim.

## Next bounded move

Trace the `exp_var_*` producer lineage beginning with Experiment 4. Do not execute notebooks or open data. Stop after confirming or rejecting the producer and mapping its output schema to the `Sigma vs log(n)` consumer.
