# `exp_var_*` Producer Lineage v0.1

**State:** REVIEW  
**Date:** 2026-07-23  
**Evidence class:** primary code inspection (notebook JSON source only); no notebooks were executed and no data files were opened.

## Task boundary

```yaml
target_artifact:
  - research/artifacts/exp_var_producer_lineage_v0_1.md
  - research/artifacts/exp_var_schema_manifest_v0_1.csv
permitted_paths:
  read: [notebooks/02_Statistical_Analysis_and_Modeling/, notebooks/06_Visualization_and_Presentation/, research/]
  write: [research/artifacts/exp_var_producer_lineage_v0_1.md, research/artifacts/exp_var_schema_manifest_v0_1.csv]
frozen_scientific_meaning: "Provenance only; no alpha, variance convention, or estimator is selected."
inputs: "Notebook JSON/source text only."
expected_outputs: "Producer-to-consumer map and schema manifest for observed exp_var_* consumer contracts."
validation_command: "Task acceptance checks and git diff --check."
forbidden_changes: "Data access, notebook execution/editing, estimator implementation, generated-output edits, and scientific interpretation."
stop_condition: "Experiment 4 confirmed/rejected for each consumer family; unmatched consumer contracts have a precise first break."
```

## Canonical notebooks inspected

| Role | Canonical path | Inspection result |
|---|---|---|
| Candidate producer | `notebooks/02_Statistical_Analysis_and_Modeling/Thesis/Experiment 4. Micro shocks. (s, gr, size dists).ipynb` | All eight cells inspected; no `exp_var_`, `to_csv`, `aggregated_simulation_results`, `var_diff_qi`, or `var_diff_agg_i` token occurs. |
| Conditional candidate | `notebooks/02_Statistical_Analysis_and_Modeling/Thesis/Experiment 3. Micro shocks. (s, gr).ipynb` | Inspected because Experiment 4 did not satisfy the consumer; writes `microshocks.csv`, not `exp_var_*`. |
| Consumer | `notebooks/06_Visualization_and_Presentation/Sigma vs log(n), q plots.ipynb` | Load/transform and immediate figure cells inspected. |

## Producer cell inventory

### Experiment 4 — rejected for the observed consumer families

- **Cell 1:** imports only.
- **Cell 3:** defines `get_clipped_lognormal`, `get_n`, and `generate_pareto_samples`.
- **Cell 5:** creates clipped lognormal and Pareto size arrays.
- **Cell 7:** runs an in-memory grid over `dist in ['norm', 'lapl']`, three size arrays, `s = np.arange(0.1, 0.8, 0.2)`, ten value-based quantiles, and 100 repetitions.  It creates `experiment_data` with columns `Distribution`, `Size_Dist`, `Shock_Intensity`, `Num_Firms`, `Repetition`, `Mean_Aggregated_Ratio`, and `Std_Aggregated_Ratio`; it contains no persistence statement.

There is consequently no Experiment 4 cell or output filename that can meet either active `exp_var_*` load contract.

### Experiment 3 — conditional inspection result

- **Cell 4:** reads `data/processed/ID_Y.csv` (not opened in this task), filters `IMPORT == 0`, and creates firm-year sales.
- **Cell 6:** defines `sizes` as firm sales totals and `parts` as a value-cumulative `Q = 10` partition.
- **Cell 8:** defines `eff_nq` as mean observed count by partition.
- **Cell 10:** defines empirical shocks from de-meaned log sales.
- **Cell 13:** sets `Q = 10`, `ss = np.arange(0.1, 0.8, 0.1)`, `M = 200`, and `T = 17`; no seed is set.
- **Cell 15:** creates `result_df` with `dist`, `s`, `mu`, `nq`, `repeat`, and ratio/log-ratio moment columns.
- **Cell 16:** writes `./../../../data/processed/microshocks.csv` with `index=False`.

This is a different output family and schema: it has neither `q`, `Q`, `i`, period columns, nor `var_diff_qi`. It does not close the break.

## Output construction and consumer contract

The live consumer load is cell 16. It expects, for each `sizes` in `pareto`, `logn90`, `logn` and each `dist` in `sbtn`, `emp_szd_T16_clip.8`, `emp_szd_T16`, `lapl`, `norm`:

- clipped empirical: `exp_var_{dist}_1s_{sizes}_7s_70Qqs_200i_.csv`;
- all other distributions: the concatenation of `exp_var_{dist}_1s_{sizes}_5s_70Qqs_200i_.csv` and `exp_var_{dist}_1s_{sizes}_2s_70Qqs_200i_.csv`.

It indexes on `s, Q, q, i`, requires string period columns `0` through `15`, selects the lowest half of repetitions by its quantile-balance rule, and cell 23 then derives `var_diff_qi` and `var_diff_agg_i`. Cells 38–39 map `q` to `n` with `get_n` and produce the `sigma_vs_n_grs.png` and `sigma_vs_n_szdists.png` figure paths.

Commented cell 7 and active cells 48–50 additionally show an older consumer contract: `exp_var_{dist}_1s_{sizes}.csv` for `dist` in `sbtn`, `lapl`, `norm`. They require at least `Q`, `q`, `s`, and `var_diff_qi`; cells 49–50 map `q` to `n` and plot log variance against log population. No producer was found under the permitted inspection order.

## Code-only variable dictionary

| Name | Definition observed in code | Status |
|---|---|---|
| `N` | `len(x1)` in consumer cells 49–50; full simulated size-array length. | DIRECT |
| `Q` | Number of value-cumulative partitions; consumer loads it as a column. | DIRECT |
| `q` | Partition/quantile index; consumer merges it to a computed `n`. | DIRECT |
| `n` | Count returned by `get_n`: `pd.cut` bins of cumulative `10**x` and `value_counts()`. | DIRECT |
| `s` | Shock-scale loop variable in both Experiment 3 and Experiment 4; consumer input column. | DIRECT |
| `i` | Consumer repetition/index field used in input index and aggregate grouping; producer definition not recovered. | PARTIAL |
| `sizes` | Consumer size-distribution label (`pareto`, `logn90`, `logn`); no producing cell recovered. | PARTIAL |
| `dist` | Consumer growth/shock-distribution label; Experiment 3 uses `norm`, `lapl`, `emp`; Experiment 4 uses `norm`, `lapl`. | PARTIAL |
| `var_diff_qi` | In cell 23, row variance over periods of bias-adjusted first differences of `log10` period values. | DIRECT |
| `var_diff_agg_i` | In cell 23, variance of bias-adjusted first differences after summing period values by `dist, sizes, s, Q, i`. | DIRECT |

## Seed and repetition audit

The relevant `exp_var_*` producer is **UNRESOLVED**, so its seed and loop count are **UNRESOLVED**. The consumer filename contract embeds `200i`; this is filename evidence only, not confirmation of a producer loop. Experiment 4 explicitly has 100 repetitions and is `UNSEEDED`; Experiment 3 explicitly has `M = 200` and is `UNSEEDED`, but neither writes the consumed family.

## Contradictions and missing links

1. Experiment 4 is described as a likely producer lead, but its source has no persistence or matching columns/filename.
2. Experiment 3 has a 200-repetition simulation but writes `microshocks.csv`; its schema is incompatible with the consumer contract.
3. The first precise unresolved break is the absent source cell that constructs and writes the consumer's period-column panel with `dist, sizes, s, Q, q, i` under an `exp_var_*` filename.

## Conclusion

**REJECTED:** Experiment 4 is not the producer of either observed `exp_var_*` consumer family. Experiment 3 does not satisfy the unmatched contracts. The direct `Sigma vs log(n)` consumer mapping is recovered, but both families remain **MISSING** on the producer side.

**Exact next pointer:** locate, without execution, the notebook or historical source cell that writes `data/processed/exp_var_{dist}_1s_{sizes}_{2s|5s|7s}_70Qqs_200i_.csv` and defines `i` plus the string period columns.

Changed:
- Added the REVIEW lineage report and schema manifest for the bounded `exp_var_*` task.
Validated:
- Notebook JSON/source inspection only; acceptance checks are reported with the task handoff.
Evidence:
- Primary notebook-source evidence described above; no data or notebook execution.
Blocked:
- The exact `exp_var_*` writer remains unresolved after the required Experiment 4 then conditional Experiment 3 inspection.
Next:
- Locate the missing writer cell for the fully specified consumer contract.
Do not open:
- Data files, notebook execution, estimator implementation, robustness work, manuscript work, P3, or repository-wide cleanup.
