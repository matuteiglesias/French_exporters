# Codex Task — Trace the `exp_var_*` Producer v0.1

**State:** READY_FOR_EXECUTION  
**Date:** 2026-07-23  
**Active front:** P2 — Concentration Is Not the Scaling Exponent

```yaml
target_artifact:
  - research/artifacts/exp_var_producer_lineage_v0_1.md
  - research/artifacts/exp_var_schema_manifest_v0_1.csv
permitted_paths:
  read:
    - notebooks/02_Statistical_Analysis_and_Modeling/
    - notebooks/06_Visualization_and_Presentation/
    - research/artifacts/
    - research/guides/
    - research/state/aggregation_reproducibility_inventory_v0_1.csv
  write:
    - research/artifacts/exp_var_producer_lineage_v0_1.md
    - research/artifacts/exp_var_schema_manifest_v0_1.csv
frozen_scientific_meaning: >
  This is a provenance task only. Do not estimate, define, reinterpret, or choose
  alpha. The current working claim remains that export variance changes with
  population size and that local bin contributions may combine through a
  covariance-adjusted effective elasticity.
inputs: >
  Repository notebook JSON and text only. Begin with Experiment 4 and inspect
  Experiment 3 only if Experiment 4 does not close the lineage. Use Sigma vs
  log(n), q plots.ipynb only as the downstream consumer contract.
expected_outputs: >
  A producer-to-consumer lineage report and a machine-readable schema manifest
  covering every observed exp_var_* output relevant to Sigma vs log(n).
validation_command: >
  Run the acceptance checks in this task, plus git diff --check. Do not run
  notebooks or read data files.
forbidden_changes: >
  No data access, notebook execution, legacy notebook edits, generated-output
  edits, estimator implementation, scientific interpretation, refactor,
  environment changes, new experiments, manuscript work, or changes outside
  the two target artifacts.
stop_condition: >
  Stop when Experiment 4 is confirmed or rejected as the producer of each
  exp_var_* family consumed by Sigma vs log(n), with every consumer mapped to
  an exact producer cell/output or marked MISSING with the first precise break.
```

## Scientific boundary

This task must not decide:

- whether alpha is variance or standard-deviation based;
- whether the displayed `1/n` line is an estimate;
- which shock family is scientifically preferred;
- whether covariance is necessary;
- whether the original result is correct;
- whether the reconstructed formal framework is novel.

## Required inspection order

### Step 1 — Experiment 4 only

Locate the canonical repository path for:

```text
Experiment 4. Micro shocks. (s, gr, size dists).ipynb
```

Extract every source cell containing any of:

```text
exp_var_
to_csv
aggregated_simulation_results
var_diff_qi
var_diff_agg_i
```

Record exact cell indices and minimal source excerpts.

### Step 2 — Output construction

For each output written or dynamically named, record:

- exact or templated filename;
- relative directory;
- dataframe variable written;
- output columns;
- index behavior;
- parameter values embedded in the filename;
- loop dimensions and repetition count;
- random seed or explicit `UNSEEDED`;
- whether the cell is active, commented, incomplete, or unreachable from prior cells.

### Step 3 — Variable dictionary

Define from code only:

```text
N
Q
q
n
s
i
sizes
dist
var_diff_qi
var_diff_agg_i
```

Use `UNRESOLVED` rather than inference when code does not define a field clearly.

### Step 4 — Consumer contract

Inspect only the load and immediate transformation cells in:

```text
Sigma vs log(n), q plots.ipynb
```

For every `exp_var_*` load statement, record:

- exact expected filename or glob;
- expected columns;
- filters immediately applied;
- derived variables immediately created;
- downstream figure or table section.

### Step 5 — Conditional Experiment 3 inspection

Inspect Experiment 3 only for a consumer entry that Experiment 4 does not satisfy.

Do not broaden beyond Experiment 3. If both fail, mark the producer `MISSING` and record the exact consumer expectation that remains unmatched.

## Markdown output schema

`research/artifacts/exp_var_producer_lineage_v0_1.md` must contain:

1. task boundary and evidence class;
2. canonical notebook paths;
3. producer cell inventory;
4. output filename construction;
5. variable dictionary;
6. producer → file → consumer map;
7. seed and repetition audit;
8. contradictions and missing links;
9. conclusion: `CONFIRMED`, `PARTIALLY_CONFIRMED`, or `REJECTED`;
10. one exact next pointer.

## CSV output schema

`research/artifacts/exp_var_schema_manifest_v0_1.csv` must contain these columns:

```text
family_id
producer_notebook
producer_cell
producer_dataframe
output_path_or_template
output_status
consumer_notebook
consumer_cell_or_context
consumer_path_or_pattern
schema_columns
parameter_dimensions
repetition_count
seed_status
lineage_status
evidence_note
```

## Acceptance checks

```bash
test -f research/artifacts/exp_var_producer_lineage_v0_1.md
test -f research/artifacts/exp_var_schema_manifest_v0_1.csv
python - <<'PY'
import pandas as pd
p = 'research/artifacts/exp_var_schema_manifest_v0_1.csv'
df = pd.read_csv(p)
required = {
    'family_id', 'producer_notebook', 'producer_cell',
    'output_path_or_template', 'output_status', 'consumer_notebook',
    'consumer_path_or_pattern', 'schema_columns', 'repetition_count',
    'seed_status', 'lineage_status', 'evidence_note'
}
missing = required - set(df.columns)
assert not missing, missing
assert len(df) > 0
assert df['consumer_notebook'].astype(str).str.contains('Sigma vs log', regex=False).any()
assert df['lineage_status'].isin([
    'CONFIRMED', 'PARTIAL', 'MISSING', 'CONTRADICTED'
]).all()
print({'rows': len(df), 'status_counts': df['lineage_status'].value_counts().to_dict()})
PY
git diff --check
```

## Handoff

```yaml
from_role: Reproducibility Engineer / Codex
to_role: Steward and PI
artifact_state: REVIEW
scientific_validation: false
next_decision: >
  Whether the recovered output lineage is sufficient to specify the common-N
  variance-accounting panel, or whether the final empirical estimator must be
  located first.
```
