# RESEARCH GROUP MOTOR — 2026-07-23 AM

## CURRENT BOTTLENECK

The original dataset is known by the PI to exist, but the repository does not yet distinguish the authoritative **generator**, **estimator**, and **presentation** code for the export variance-decay exponent. Running notebooks now would risk reproducing a nearby simulation rather than the flagship result.

## TODAY'S MOVE

```yaml
mode: BUILD
lead_player: Reproducibility Engineer
supporting_players:
  - Archivist
  - Methodkeeper
objective: Freeze a data-free code-role map and experiment contract for AGG-ALPHA-EXPORT.
completion_condition: >
  Candidate code is classified by role; the minimum input schema and transformation
  chain are recorded; unresolved scientific choices are explicit; and the next Codex
  task can proceed without access to the confidential data.
```

## WORK PERFORMED

Repository code search and direct notebook inspection produced the following map.

### 1. Input consumers

A repository search for `ID_Y.csv` returns many consumers across exploratory, time-series, preliminary, and thesis notebooks. This confirms that `ID_Y.csv` is a shared analysis panel rather than an Experiment-5-specific artifact.

Minimum columns directly observed in the flagship neighborhood:

| Column | Observed use |
|---|---|
| `IMPORT` | Select export observations with `IMPORT == 0` |
| `ID` | Firm identifier used in firm-year aggregation |
| `YEAR` | Time index used to construct the firm panel |
| `VART` | Trade value summed by firm and year |

The actual data and additional columns are deliberately outside this play.

### 2. Candidate generator

`notebooks/02_Statistical_Analysis_and_Modeling/Thesis/Experiment 5. Simple var vs nq, s. (s).ipynb`

Observed responsibilities:

- reads `ID_Y.csv`;
- filters exports;
- forms a firm-by-year value matrix;
- computes demeaned log firm values and empirical microshock dispersion;
- constructs cumulative-value groups;
- simulates shocks at several magnitudes;
- calculates group variance measures;
- writes `aggregated_simulation_results.csv`.

Classification: **simulation/result generator candidate**, not yet the authoritative alpha estimator.

Reasons not to promote it:

- random draws are unseeded;
- output path in code differs from the committed candidate output location;
- the notebook contains a duplicated variance-construction line;
- no inspected cell estimates the reported export alpha directly.

### 3. Candidate empirical decomposition

`notebooks/02_Statistical_Analysis_and_Modeling/PreliminaryStudies/Linear Base + Noise decomposition.ipynb`

Observed responsibilities:

- reads `ID_Y.csv` and filters exports;
- creates cumulative-value partitions;
- decomposes values into base, common, and noise components;
- computes variance and covariance matrices across groups.

Classification: **mechanism/decomposition candidate**. It may support AGG-VAR-DECOMP but is not yet identified as the export-alpha estimator.

### 4. Candidate presentation and slope neighborhood

`notebooks/06_Visualization_and_Presentation/Sigma vs log(n), q plots.ipynb`

Observed responsibilities:

- loads families of simulation outputs named `exp_var_*`;
- excludes highly unbalanced partition draws;
- creates group-population counts `n` from equal-value partitions;
- merges `n` with group variance `var_diff_qi`;
- plots variance against population on log-log axes;
- compares results to a `1/n` reference;
- writes paper figure paths including `sigma_vs_n_grs.png` and `sigma_vs_n_szdists.png`.

Classification: **presentation and possible estimator neighborhood**. It is currently the closest inspected code to the scientific object “variance versus population size,” but the inspected cells plot medians and reference lines rather than freeze a regression estimator.

### 5. Surviving output evidence

`notebooks/bkp_misc_data/exp_var_norm_1s.csv` is a Git LFS object:

```text
oid sha256: ad455420518ed682e8bb380cdf05b8975477a75992937aa2524423e95834e0d5
size: 69397 bytes
```

This is an inspectable provenance lead, not a verified flagship output.

### 6. Repository-level evidence

`Notes/summary_code_nbs.md` records a notebook called `Decomposition terms. w Bootstrap.ipynb` using groupby, covariance, `polyfit`, and `log10` to relate self-variance and population size. The current canonical path was not located through direct fetch. This is a high-priority archaeology target because it may contain the missing estimator.

## DATA-FREE EXPERIMENT CONTRACT — REVIEW

```yaml
claim_id: AGG-ALPHA-EXPORT
scientific_object: export idiosyncratic variance decay with group population size
reported_result: alpha approximately 0.48-0.50
sign_convention: unresolved

input_contract:
  dataset_role: analysis-ready confidential firm-year trade panel
  known_required_columns:
    IMPORT: flow flag; exports observed as IMPORT == 0
    ID: firm identifier
    YEAR: time index
    VART: trade value
  data_location: supplied later by PI; out of scope now

observed_transformations:
  - filter exports
  - aggregate VART by firm and year
  - form firm-by-year panel
  - define firm size using a sum or mean over time; authoritative choice unresolved
  - order firms by size
  - create groups using cumulative-value cuts; exact accepted algorithm unresolved
  - calculate group population n
  - define idiosyncratic firm fluctuations; exact accepted definition unresolved
  - aggregate fluctuations to group-level variance
  - estimate log variance dependence on log n

estimator_contract_unresolved:
  dependent_variable:
    candidates:
      - variance
      - standard deviation
      - variance of log differences
      - variance of exact nominal deviations
  independent_variable: group population n
  regression_scale: expected log-log; not yet frozen
  weighting: unresolved
  included_groups: unresolved
  repetition_aggregation: unresolved
  uncertainty: unresolved
  alpha_mapping: unresolved sign and variance-versus-standard-deviation convention

no_data_acceptance_test:
  - all candidate notebooks are classified as generator, estimator, mechanism, or presentation
  - every `ID_Y.csv` consumer relevant to P2 is inventoried
  - every `exp_var_*`, bootstrap, and variance-population output family is tied to at least one producer or marked orphaned
  - exact code cells containing `polyfit`, regression, or fitted slopes are extracted
  - no scientific default is silently selected
```

## SCIENTIFIC SIGNIFICANCE

The repository contains multiple related experiments. Treating the first executable notebook as authoritative would create a false reproduction. The present map reduces that risk by distinguishing computational roles and isolating the missing scientific contract: what exactly was regressed, across which groups and repetitions, and how the fitted slope maps to alpha.

## PI HUMAN RESEARCH HOUR

```yaml
question_or_decision: >
  Which surviving notebook or figure do you remember as the source of the
  published-intent export variance-decay result?
primary_artifact: research/plays/2026-07-23_AM_export_alpha_code_map_v0_1.md
why_this_unlocks_the_bottleneck: >
  Repository evidence has narrowed the search to generator, decomposition,
  and sigma-versus-n presentation neighborhoods. PI recognition can select
  the authoritative lineage without opening the data.

minute_plan:
  - minutes: 0-10
    action: Read the code-role map and reject any materially wrong classification.
  - minutes: 10-25
    action: Browse only the named candidate notebooks and their visible figures/markdown; do not execute cells.
  - minutes: 25-40
    action: Identify the figure, notebook, or filename you recognize as the intended alpha result.
  - minutes: 40-50
    action: Write 5-10 lines defining what alpha measured: variance or standard deviation, exact or linear shocks, group construction, and export sample.
  - minutes: 50-57
    action: Record the best remembered source path and any uncertain alternatives in this play document or a new PI note.
  - minutes: 57-60
    action: Leave one line beginning `Next:` with the selected object and completion condition.

expected_evidence:
  - one preferred authoritative notebook/figure lineage or an explicit `unknown`
  - a short remembered estimand definition
  - rejected candidate paths, if any
  - one exact next pointer

stop_condition: >
  Stop after one lineage is selected or after all three candidate neighborhoods
  are explicitly marked unrecognized. Do not begin debugging or data loading.

do_not_open:
  - confidential source data
  - full manuscript rewrite
  - literature search
  - environment modernization
  - repository-wide notebook cleanup
  - P3
```

## CODEX PACKET

See `research/codex/2026-07-23_export_alpha_archaeology_task_v0_1.md`.

## PI UNLOCK

No research-direction decision is required before Codex performs the bounded archaeology task. PI recognition during the hour can improve prioritization but is not required for code inventory.

## NEXT POINTER

Run the Codex archaeology packet against `master`; review its code-role manifest and extracted estimator snippets before allowing any code execution or refactor.

## LABORATORY STATE

```yaml
active_front: P2 — Concentration Is Not the Scaling Exponent
mode: BUILD
primary_artifact: research/plays/2026-07-23_AM_export_alpha_code_map_v0_1.md
artifact_state: REVIEW
original_data_status: PI confirms available; deliberately not accessed in this phase
current_bottleneck: authoritative estimator and estimand lineage unresolved
wip: 1
next_executor: Codex under AGENTS.md contract
```
