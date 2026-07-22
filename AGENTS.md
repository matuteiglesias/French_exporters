# AGENTS.md — French Exporters research recovery

## Mission

Recover a defensible, executable evidence chain for the active paper candidate **P2 — Concentration Is Not the Scaling Exponent**.

The immediate gate is the **export variance-decay exponent**. Do not broaden the project until that result has a mapped input, sample construction, executable code path, output artifact, estimate, uncertainty, and exact blocker or reproduction status.

## Authority boundary

Matías Iglesias is the Principal Investigator. Codex and other AI tools are implementation executors, not scientific authorities or authors.

Do not independently change:

- the research question or active front;
- estimands, samples, variable meanings, or identification claims;
- interpretation, novelty, publication framing, or authorship;
- data-release policy or external communication.

When a scientific choice is ambiguous, stop with a concise decision packet rather than selecting silently.

## Evidence rules

Classify every substantive statement as primary evidence, source claim, derived result, inference, or speculation.

Never claim a file, dataset, command, experiment, or result was inspected or run unless it actually was. Unknown and blocked are valid outcomes.

All AI-produced artifacts enter `REVIEW` unless an objective, pre-authorized acceptance test passes.

## Work-in-progress rule

Keep one active research artifact. Current primary artifact:

`research/state/aggregation_reproducibility_inventory_v0_1.csv`

Do not open P3, manuscript-wide rewrites, journal targeting, broad literature scans, or unrelated notebook cleanup.

## First engineering objective

Map the export-alpha chain from legacy notebooks and data artifacts.

Known candidate paths include:

- `notebooks/02_Statistical_Analysis_and_Modeling/Thesis/Experiment 5. Simple var vs nq, s. (s).ipynb`
- `notebooks/02_Statistical_Analysis_and_Modeling/Thesis/Covariance Terms Bootstrap Experiments.ipynb`
- `notebooks/bkp_misc_data/exp_var_norm_1s.csv`
- `notebooks/02_Statistical_Analysis_and_Modeling/Thesis/aggregated_simulation_results.csv`
- `data/bootstraps/`
- expected-but-currently-unresolved `data/processed/ID_Y.csv`

Treat notebook prose and old generated summaries as leads, not verified evidence.

## Required task specification

Before implementation, record:

```yaml
target_artifact:
permitted_paths:
frozen_scientific_meaning:
inputs:
expected_outputs:
validation_command:
forbidden_changes:
stop_condition:
```

## Coding rules

- Prefer extraction of small testable modules over editing notebook cells in place.
- Preserve original notebooks and outputs as archival evidence.
- Put new reusable code under `src/` and tests under `tests/`.
- Do not silently repair data or replace missing files with synthetic data.
- Make randomness explicit and seeded.
- Record environment and dependency assumptions.
- Produce machine-readable outputs and a short failure report.
- Avoid repository-wide formatting or notebook normalization during evidence recovery.

## Completion evidence

A task is complete only with one of:

1. a reproducible command and validated output;
2. an updated inventory row with inspected provenance;
3. a precise first failure, including command, traceback/error, missing dependency, and next bounded action.

End every task with:

```text
Changed:
Validated:
Evidence:
Blocked:
Next:
Do not open:
```
