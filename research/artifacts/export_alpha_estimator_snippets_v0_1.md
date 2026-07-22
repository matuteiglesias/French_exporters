# Export-alpha estimator snippets v0.1 — REVIEW

```yaml
target_artifact: research/artifacts/export_alpha_code_role_manifest_v0_1.csv and research/artifacts/export_alpha_estimator_snippets_v0_1.md
permitted_paths: [research/artifacts/, research/state/]
frozen_scientific_meaning: "Export idiosyncratic variance decays with group population size, with reported alpha approximately 0.48–0.50."
inputs: "Repository text and notebook JSON only; no data files opened and no notebooks executed."
expected_outputs: "Role manifest and smallest code excerpts for competing estimator implementations."
validation_command: "Acceptance-test commands in research/codex/2026-07-23_export_alpha_archaeology_task_v0_1.md"
forbidden_changes: "No data access, notebook execution, scientific choice, or legacy-file edits."
stop_condition: "Artifacts pass acceptance checks; authoritative estimator lineage remains unresolved."
```

**Evidence classification:** all entries below are **primary code evidence** copied from notebook source; the metadata labels are engineering descriptions in `REVIEW`, not scientific conclusions.

## S1 — simulation group variance

```yaml
path: notebooks/02_Statistical_Analysis_and_Modeling/Thesis/Experiment 5. Simple var vs nq, s. (s).ipynb
cell_index_or_context: 4
inputs: "ID_Y.csv: IMPORT, ID, YEAR, VART."
calculation: "Export-only firm-year sales; sorted cumulative-sales quantile groups; variance across time for total, noise, and base group sums."
outputs: "yqs_var, noise_var, base_var, q, nqs, s, m."
scientific_choice_embedded: "IMPORT == 0; nonpositive sales replaced with NaN; quantile grouping uses cumulative total sales; fixed s grid."
uncertainty: "No fitted slope or uncertainty interval; random choice is unseeded."
```

```python
sales_data = df[df['IMPORT'] == 0].groupby(['ID', 'YEAR'])['VART'].sum().unstack()
sales_data = sales_data.loc[sales_data.sum(axis=1).sort_values().index]
# ...
total['q'] = pd.cut(total.sum(axis=1).cumsum(), num_quantiles, labels=range(num_quantiles))
noise_qs = noise.groupby(total['q']).sum()
base_qs = base.groupby(total['q']).sum()
yqs = noise_qs + base_qs
out = pd.concat([yqs.var(axis=1), noise_qs.var(axis=1), base_qs.var(axis=1)], axis=1)
out.columns = ['yqs_var', 'noise_var', 'base_var']
out['q'] = range(num_quantiles); out['m'] = m; out['nqs'] = total['q'].value_counts().values; out['s'] = s;
```

## S2 — exp_var log-difference variance construction

```yaml
path: notebooks/06_Visualization_and_Presentation/Sigma vs log(n), q plots.ipynb
cell_index_or_context: 23
inputs: "Loaded exp_var_* rows with period columns 0..T, dist, sizes, s, Q, q, i."
calculation: "Assigns distribution-specific slope constants, subtracts a period bias from log10 differences, then calculates variance by row."
outputs: "var_diff_qi and var_diff_agg_i."
scientific_choice_embedded: "Hard-coded distribution-specific slope constants; selected distributions and period count."
uncertainty: "No estimator uncertainty calculated."
```

```python
diff = np.log10(df[[str(t) for t in range(T + 1)]]).diff(axis = 1)
bias = pd.DataFrame(np.array((T + 1)*[-df['slope'].values]).T*range(T + 1))
bias.columns = diff.columns
df['var_diff_qi'] = (diff - bias).var(1)
# ...
diff_agg = grouped[[str(t) for t in range(T + 1)]].apply(lambda x: np.log10(x.sum()).diff())
bias_agg = pd.DataFrame(np.array((T + 1)*[-grouped['slope'].first().values]).T*range(T + 1))
df_agg = (diff_agg - bias_agg).var(1)
df_agg.name = 'var_diff_agg_i'
```

## S3 — fitted bias slopes

```yaml
path: notebooks/06_Visualization_and_Presentation/Sigma vs log(n), q plots.ipynb
cell_index_or_context: 21
inputs: "exp_var-derived panel restricted to pct < .2."
calculation: "Fits period-index slopes to log10 group means, then fits mean absolute slope against s squared."
outputs: "slopes, bias_slope, printed polyfit coefficients."
scientific_choice_embedded: "pct < .2 restriction; absolute-value transformation; group means; s squared fit."
uncertainty: "No standard errors or confidence interval."
```

```python
df['pct'] = (df['q'] + .5)/df['Q']
df = df.loc[df.pct < .2]
linear_bias = df.groupby(['dist', 'sizes', 's', 'Q', 'q'])[[str(t) for t in range(T + 1)]].apply(lambda x: np.log10(x).mean().diff()).dropna(axis = 1)
linear_bias.columns = linear_bias.columns.astype(int)
slopes = linear_bias.T.apply(lambda x: np.polyfit(linear_bias.columns, x, 1)[0])
slopes = pd.DataFrame(abs(slopes), columns = ['slope'])
bias_slope = slopes.groupby(['sizes','dist', 's'])['slope'].mean().reset_index()
bias_slope['s2'] = bias_slope['s']**2
print(np.polyfit(part.s2, part.slope,1))
```

## S4 — construction of `n` and variance-vs-population presentation

```yaml
path: notebooks/06_Visualization_and_Presentation/Sigma vs log(n), q plots.ipynb
cell_index_or_context: 38
inputs: "full_data exp_var-derived rows; x_logn_clip3; Q=10."
calculation: "Maps q to `n` using get_n, calculates log_n, summarizes var_diff_qi by n, and overlays a 1/n reference."
outputs: "sigma_vs_n_grs.png in an external relative path."
scientific_choice_embedded: "Q=10; lognormal size distribution; chosen distribution lists and every-other s selection; quartile summaries."
uncertainty: "Interquartile fill only; no slope fit or alpha mapping in this cell."
```

```python
bins, ns = get_n(x_logn_clip3, Q_)
ns = pd.DataFrame([range(Q_), ns], index = ['q', 'n']).T
result = result.merge(ns, on = 'q')
result['log_n'] = np.log10(result.n)
y = 'var_diff_qi'
bin_vals = sorted_s.groupby('n')['var_diff_qi'].describe()
xn = bin_vals.index.values
ax.plot([xn.min(), xn.max()], [.0002/xn.min(), .0002/xn.max()], label = '1/n dependence', linestyle = '--')
```

## S5 — transformed exp_var scatter presentation

```yaml
path: notebooks/06_Visualization_and_Presentation/Sigma vs log(n), q plots.ipynb
cell_index_or_context: 49–50
inputs: "exp_var_*.csv: Q, q, var_diff_qi, s; simulated size arrays."
calculation: "Maps q to n; transforms variance to log10 variance and normalizes by s squared in the second variant."
outputs: "Scatter plot files in external relative paths."
scientific_choice_embedded: "Q=25; selected distributions, size arrays, s values, jitter and plot limits."
uncertainty: "No fitted slope; unseeded jitter via np.random.normal."
```

```python
df['t'] = df['var_diff_qi']/(df['s']**2)
bins, ns = get_n(x1, Q_)
ns = pd.DataFrame([range(Q_), ns], index = ['q', 'n']).T
df = df.merge(ns)
df['log_n'] = np.log10(df.n)
df['log_var_diff_qi'] = np.log10(df.var_diff_qi) - np.log10(s**2)
data = df[df.s == s].sample(frac = frac); data.log_n = data.log_n + np.random.normal(0, 0.03, len(data))
```

## S6 — covariance notebook partition construction

```yaml
path: notebooks/02_Statistical_Analysis_and_Modeling/Thesis/Covariance Terms Bootstrap Experiments.ipynb
cell_index_or_context: 30
inputs: "ID_Y.csv: IMPORT, ID, YEAR, VART."
calculation: "Export-only firm-year sales, demeaned log sales, sales-size ordering, and cumulative-size partitions."
outputs: "sales, logsales, demlogsales, sizes, parts."
scientific_choice_embedded: "IMPORT == 0; Q=10; sizes based on total sales; cumulative-size partitioning."
uncertainty: "No uncertainty calculation in this excerpt."
```

```python
df = pd.read_csv('./../../data/processed/ID_Y.csv')
sales = df.loc[df.IMPORT == 0].groupby(['ID', 'YEAR'])['VART'].sum().unstack()
sales = sales.loc[sales.sum(1).sort_values().index]
logsales = np.log10(sales)
demlogsales = logsales.subtract(logsales.mean(1), axis = 0)
sizes = sales.loc[sales.sum(1).sort_values().index].sum(1)
Q = 10
parts = pd.cut(sizes.cumsum()/sizes.sum(), Q, labels = range(Q)).sort_index()
```

## Unresolved choices and lineage status

* **Inference from inspected code:** no snippet maps any fitted slope to an `alpha` label. The competing slope code fits bias/plot relationships, not an explicitly named export-alpha estimate.
* **Exact decisions retained for the PI:** variance versus standard deviation as dependent variable; slope sign and alpha mapping; source/validity of hard-coded bias slopes; authoritative output family and producer; group construction and filtering; weighting and uncertainty estimator; choice among empirical versus simulated shocks and partition variants.
* **Orphaned families:** `exp_var_*` (expected `data/processed` paths, no actual producer found), notebook-local `aggregated_simulation_results.csv`, `exp_var_norm_1s.csv`, `cov_elements_desc_*`, `parts_cross_cov_*`, `bs_base_*`, `bs_totl_*`, and repository-path `sigma_vs_n_*.png`.

```yaml
from_role: Codex / Reproducibility Engineer
to_role: Steward
artifact:
  - research/artifacts/export_alpha_code_role_manifest_v0_1.csv
  - research/artifacts/export_alpha_estimator_snippets_v0_1.md
state: REVIEW
verified: acceptance tests only
open_uncertainties: "See unresolved choices and lineage status above."
decision_needed: "Whether PI can identify the authoritative estimator lineage."
next_action: "Review manifest before execution or refactor."
stop_condition: "One authoritative lineage selected or explicit unresolved shortlist retained."
```
