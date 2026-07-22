# Codex Task — Export Alpha Code Archaeology v0.1

## Role

Act as a bounded Reproducibility Engineer under `AGENTS.md`. This is code archaeology only. Do not access, request, synthesize, or substitute the confidential source data.

## Target artifact

Create:

```text
research/artifacts/export_alpha_code_role_manifest_v0_1.csv
research/artifacts/export_alpha_estimator_snippets_v0_1.md
```

## Permitted paths

Read anywhere in the repository.

Write only under:

```text
research/artifacts/
research/state/
```

Do not modify legacy notebooks, data, figures, governance files, or manuscript material.

## Frozen scientific meaning

The active claim is:

> Export idiosyncratic variance decays with group population size, with reported alpha approximately 0.48–0.50.

Do not decide whether the dependent variable should be variance or standard deviation. Do not choose a sign convention, sample filter, grouping algorithm, weighting rule, or accepted estimator. Record competing implementations separately.

## Work specification

### A. Inventory relevant files

Search repository text and notebook JSON for at least these terms:

```text
ID_Y.csv
IMPORT == 0
var_diff_qi
log_var_diff_qi
polyfit
linregress
OLS
log_n
sigma_vs_n
exp_var_
cov_elements_desc
parts_cross_cov
bs_base
bs_totl
1/n dependence
```

For every relevant file, record:

```csv
path,file_type,role,input_references,output_references,key_symbols,contains_fit,contains_randomness,seed_observed,status,notes
```

Allowed role values:

```text
INPUT_PRODUCER
GENERATOR
ESTIMATOR
MECHANISM
PRESENTATION
SUMMARY_ONLY
CHECKPOINT_OR_DUPLICATE
ORPHAN_OUTPUT
UNCLASSIFIED
```

### B. Trace `ID_Y.csv`

Inventory every consumer and every possible producer. A producer must contain an actual write operation targeting `ID_Y.csv` or a clearly equivalent renamed path. Mentions in prose do not count as producers.

Record the minimum columns each consumer uses.

Do not infer that similarly shaped files are substitutes.

### C. Trace output families

For each family below, identify producers and consumers or mark it orphaned:

```text
exp_var_*
aggregated_simulation_results.csv
exp_var_norm_1s.csv
cov_elements_desc_*
parts_cross_cov_*
bs_base_*
bs_totl_*
sigma_vs_n_*.png
```

### D. Extract estimator snippets

Copy only the smallest relevant code snippets containing:

- fitted slopes or regressions;
- `polyfit`, `linregress`, OLS, or equivalent calculations;
- construction of `n` or `log_n`;
- construction of variance, standard deviation, or log-difference variance;
- mapping from a fitted slope to an alpha label, if present.

For each snippet include:

```yaml
path:
cell_index_or_context:
inputs:
calculation:
outputs:
scientific_choice_embedded:
uncertainty:
```

Do not rewrite or improve the code.

### E. Update state

Update `research/state/aggregation_reproducibility_inventory_v0_1.csv` only if it exists on the working branch. Add inspected candidate paths and replace the first blocker with the precise remaining lineage ambiguity. Do not set `can_reproduce_now=YES`.

## Acceptance tests

Run and report commands equivalent to:

```bash
test -f research/artifacts/export_alpha_code_role_manifest_v0_1.csv
test -f research/artifacts/export_alpha_estimator_snippets_v0_1.md
python - <<'PY'
import csv
from pathlib import Path
p = Path('research/artifacts/export_alpha_code_role_manifest_v0_1.csv')
rows = list(csv.DictReader(p.open()))
assert rows
assert any('ID_Y.csv' in (r.get('input_references') or '') for r in rows)
assert any((r.get('contains_fit') or '').upper() == 'YES' for r in rows)
assert all(r.get('role') for r in rows)
print(len(rows))
PY
```

Also report:

- number of files inventoried;
- number of actual `ID_Y.csv` producers found;
- number of fitting/estimator snippets found;
- orphaned output families;
- exact unresolved scientific choices.

## Forbidden changes

- no data access or fabricated sample data;
- no notebook execution;
- no dependency installation;
- no notebook cleaning or formatting;
- no extraction into production modules yet;
- no claim interpretation;
- no manuscript edits;
- no P3 work;
- no changes outside permitted write paths.

## Stop condition

Stop when the two target artifacts pass the acceptance tests, or when repository access prevents text inspection. On failure, record the exact inaccessible path or tool limitation. Do not broaden the task.

## Handoff

```yaml
from_role: Codex / Reproducibility Engineer
to_role: Steward
artifact:
  - research/artifacts/export_alpha_code_role_manifest_v0_1.csv
  - research/artifacts/export_alpha_estimator_snippets_v0_1.md
state: REVIEW
verified: acceptance tests only
open_uncertainties: list exact scientific choices and orphaned lineages
decision_needed: whether PI can identify the authoritative estimator lineage
next_action: review manifest before execution or refactor
stop_condition: one authoritative lineage selected or explicit unresolved shortlist retained
```
