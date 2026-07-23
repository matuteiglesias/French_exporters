# Research Group Motor — 2026-07-23 PM

## Mode

**ADVANCE**

## Formation

- Lead: Steward
- Scientific authority: Principal Investigator
- Supporting roles: Methodkeeper, Reproducibility Engineer, Critic, Finisher

Roles were executed sequentially and do not imply autonomous parallel work.

## Completed PI hour

The PI completed the planned one-hour research session and reached the stop condition without opening confidential data, executing notebooks, refactoring legacy code, or expanding into a manuscript rewrite.

The hour produced:

- a formal framework for nonlinear micro-to-macro aggregation;
- a synthesis map connecting thesis formulas, experiments, figures, code, and unresolved links;
- a research-hour close with a falsifiable next test;
- a clarified PI direction distinguishing local subpopulation alphas from the effective whole-population alpha.

## State change

The active front is no longer blocked by the absence of any coherent estimand interpretation.

It is now in **formal reconstruction and lineage closure**.

The strongest current working synthesis is:

> The whole-population export alpha is a covariance-adjusted, contribution-weighted, scale-dependent effective elasticity. It reduces to a common part alpha under common-exponent assumptions and approximates a contribution-weighted combination of heterogeneous part alphas only under restrictive conditions.

This synthesis remains REVIEW. It is not yet a validated empirical result or novelty claim.

## Evidence produced

### PI evidence

The PI accepted the direction of reconstructing whole-population alpha from segment contributions and covariance terms rather than forcing a single uniquely authoritative scalar estimator.

### Thesis and code evidence

The recovered materials support:

- common-alpha inheritance under common-exponent assumptions;
- nonlinear micro-moment effects;
- equal-value population grouping;
- group variance construction;
- variance-versus-population figures;
- base/noise and covariance outputs.

### Derived result

The heterogeneous-alpha and covariance-adjusted aggregation identities are mathematical completions in REVIEW.

### Remaining breaks

1. exact `exp_var_*` producer and schema;
2. final empirical export-alpha estimator and sign convention;
3. common-`N` accounting panel for direct versus reconstructed alpha.

## Artifact classification

### REVIEW

- `research/artifacts/export_alpha_research_hour_close_v0_1.md`
- `research/artifacts/export_alpha_framework_integration_v0_1.md`
- source synthesis map supplied by the PI research hour
- source formal framework compendium supplied by the PI research hour
- `research/guides/french_exporters_notebook_atlas_v0_1.md`

### ACCEPTED PI decisions

- P2 remains the only active research-output front.
- The local-to-global aggregation question is the central scientific target.
- The direct-versus-reconstructed alpha comparison is the accepted next empirical adjudication.
- Manuscript expansion and novelty claims remain gated behind reproducibility and validation.

### BLOCKED

- reproduced empirical export alpha;
- covariance-adjusted reconstruction;
- paper-level claim freeze.

## Publication development path

The laboratory should progress through the following gates without opening a second output front:

1. close output lineage;
2. freeze estimands, population path, and validation tolerance;
3. reproduce the direct empirical coefficient;
4. construct and test the full variance-accounting identity;
5. conduct adversarial robustness only after the central test works;
6. perform targeted novelty and literature adjudication;
7. freeze the paper claim and build manuscript plus replication package;
8. select venue and submit.

The laboratory is therefore already building a paper, but it is doing so through evidence-bearing gates rather than prose accumulation.

## Next bounded executor move

Run:

```text
research/codex/2026-07-23_trace_exp_var_producer_task_v0_1.md
```

The task may inspect notebook source only. It must confirm or reject Experiment 4 as the producer of the `exp_var_*` families and map every relevant output to the `Sigma vs log(n)` consumer.

## Completion condition for the next play

- Experiment 4 classified as confirmed, partial, or rejected producer;
- every observed `exp_var_*` consumer mapped to a producer output or a precise missing break;
- schema, parameters, repetition count, and seed status recorded;
- no data opened and no notebook executed.

## Stop condition

Stop after the lineage report and schema manifest pass their engineering checks. Do not proceed to estimator implementation or the common-`N` panel in the same play.

## Do not open

- confidential data;
- notebook execution;
- final estimator implementation;
- robustness grid;
- literature novelty scan;
- manuscript-wide writing;
- journal targeting;
- P3;
- repository-wide cleanup.
