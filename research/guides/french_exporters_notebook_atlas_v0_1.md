# French Exporters Notebook Atlas v0.1 — REVIEW

**Purpose:** help the PI, steward, and bounded Codex agents navigate the legacy notebook archive without treating filenames, old summaries, or the first executable notebook as scientific authority.

**Active use:** P2 — *Concentration Is Not the Scaling Exponent*.

**Evidence rule:** direct code inspection and current research artifacts outrank the old automated notebook summaries. The summary files are useful for recall and search only; they contain visible misclassifications.

## Confidence labels

- **A — directly inspected:** role supported by notebook source or current code-archeology artifacts.
- **B — strong navigation lead:** role supported by repository summaries, filenames, output families, and related code, but the notebook still needs direct inspection.
- **C — adjacent or legacy lead:** potentially useful later; not part of the immediate export-alpha chain.
- **D — duplicate/noise:** checkpoint, backup, recovered blob, obsolete copy, or misleading summary. Open only when the canonical path is missing.

---

# 1. The shortest P2 reading route

Use this order for the first serious reconstruction pass.

| Order | Notebook or artifact | Role | Why open it | Confidence |
|---:|---|---|---|---|
| 0 | `research/artifacts/export_alpha_estimator_snippets_v0_1.md` | Existing map | Six minimal primary-code excerpts and unresolved estimator choices. | A |
| 1 | `Gabaix Equations Review.ipynb` | Theory/intellectual scratchpad | Pareto tails, Herfindahl/concentration, Levy/Gaussian behavior, and the theoretical scaling intuition. Treat as derivation notes, not a final theorem statement. | B |
| 2 | `Test Exercise Gabaix Riccaboni.ipynb` | Empirical precursor | Increasing-population samples, Pareto structure, fluctuations versus population size, and candidate log-log scaling. Likely one of the closest early empirical statements of the result. | B |
| 3 | `Growth rates as shocks from mean.ipynb` | Micro-moment measurement | Firm-size, export status, log fluctuations, yearly/quarterly growth, and moments needed to parameterize simulations. | B |
| 4 | `Save Growth info.ipynb` | Upstream moment/panel builder | Constructs standardized firm-size and growth-rate information used downstream. | B |
| 5 | `Experiment 3. Micro shocks. (s, gr).ipynb` | Microshock simulation | Applies empirical/theoretical shock distributions to grouped firm populations; useful for understanding how local moments generate aggregate variance. | B |
| 6 | `Experiment 4. Micro shocks. (s, gr, size dists).ipynb` | Controlled simulation grid | Combines Pareto/lognormal size distributions with Gaussian, Laplace, Subbotin, and empirical shock families. Likely producer or precursor of `exp_var_*` result families. | B |
| 7 | `Experiment 5. Simple var vs nq, s. (s).ipynb` | Group-variance generator | Reads the firm-year panel, filters exports, constructs cumulative-value groups, simulates shocks, calculates group variances, and writes aggregated simulation results. It is **not yet** the authoritative alpha estimator. | A |
| 8 | `Sigma vs log(n), q plots.ipynb` | Variance–population presentation and estimator neighborhood | Loads `exp_var_*`, constructs group population `n`, computes/uses `var_diff_qi`, and produces variance-versus-`n` paper figures. Closest inspected location to the final visual argument. | A |
| 9 | `Partial dependence Analysis.ipynb` | Local-to-aggregate bridge | Investigates dependence and partial derivatives of total variance with respect to population size under different distributions and shock scales. Highly relevant to the PI’s current subpopulation-alpha synthesis. | B |
| 10 | `Linear Base + Noise decomposition.ipynb` | Mechanism decomposition | Separates base, common, and noise components and calculates variance/covariance matrices across cumulative-value groups. | A |
| 11 | `Covariance Terms Bootstrap Experiments.ipynb` | Empirical covariance decomposition | Builds export-only partitions and explores diagonal/off-diagonal covariance contributions. | A |
| 12 | `Experiment 2. Extensive BME.ipynb` | Bootstrap decomposition engine | Generates and characterizes base/noise/common and cross-covariance output families. Important when the aggregate alpha requires covariance corrections. | B |
| 13 | `Decomposition terms. w Bootstrap.ipynb` | Missing/legacy estimator candidate | Repository notes describe `polyfit`, `log10`, self-variance, population `n`, covariance, boxplots, and heatmaps. Locate its canonical or historical blob before assuming it is lost. | B / unlocated |
| 14 | `Std of quantiles.ipynb` | Economic interpretation / empirical figure lead | Likely summarizes volatility by quantile and may connect group-level moments to the argument presented in the thesis. | B |

## Immediate research interpretation

The core chain is probably not one notebook:

```text
micro moments and firm-size distributions
    -> synthetic or empirical group construction
    -> group variance and covariance outputs
    -> map quantile/group to population n
    -> local variance-versus-n relationships
    -> combination across subpopulations and covariance terms
    -> effective whole-population alpha
    -> paper figure and argument
```

---

# 2. P2 notebook families

## A. Theory and mathematical intuition

### `Gabaix Equations Review.ipynb`

**Use for:**
- Pareto and lognormal size distributions;
- Herfindahl behavior as population grows;
- Levy/Gaussian aggregation intuition;
- checking whether concentration and volatility scaling are being conflated;
- recovering notation and remembered derivations.

**Do not assume:** every simulation or plotted slope in this notebook is the accepted estimator.

### `Gabaix numerical tests.ipynb`

**Use for:** numerical experiments on shocks, levels, linear approximations, Levy behavior, Herfindahl expressions, and Gabaix-style decay propositions.

**Relationship:** theoretical sandbox supporting the intuition behind Experiments 3–5.

### `Log of sum of powers.ipynb`

**Use for:** understanding how sums of exponentiated shocks behave as `N` grows under Pareto, lognormal, Gaussian, or Laplace assumptions.

**Relationship:** mathematical sanity check for aggregation under fat-tailed size and shock distributions.

### `Herfindahl (Nieuwerburgh).ipynb`

**Use for:** concentration baselines and the mapping from size-distribution moments to Herfindahl-type quantities.

**Warning:** concentration is a comparator or mechanism variable, not automatically the scaling exponent.

### `Test Exercise Gabaix Riccaboni.ipynb`

**Use for:**
- near-Pareto empirical sizes;
- increasing sample/group population;
- fluctuations of aggregated exports/imports;
- quantile-specific variance/standard-deviation behavior;
- early bootstrap and regression ideas.

**Priority:** very high for remembering the original argument, even if later notebooks superseded its estimator.

---

## B. Firm sizes and micro moments

### `Dataset totals.ipynb`

**Use for:** overall data sanity, export/import totals, size distributions, descriptive statistics, and synthetic Gabaix-style comparisons.

### `Size distribution (legacy).ipynb`

**Use for:** empirical size CDFs, top agents, counts versus value, and old figures that may have entered the thesis.

### `Parabolas. Simulated distribution and growth.ipynb`

**Use for:**
- fitting the body/tail of the firm-size distribution;
- deriving simulated Pareto/lognormal populations;
- empirical growth-rate distributions;
- small-versus-large firm growth differences;
- parameters later reused in Experiments 3–5 and `Sigma vs log(n)`.

### `Growth rates as shocks from mean.ipynb`

**Use for:** defining empirical microshocks, firm-level deviations, growth distributions, and size-dependent moments.

### `Growth rates.ipynb`

**Use for:** broad exploratory distributions of firm growth, counts, values, and the top tail. Treat as an upstream empirical exploration rather than the final estimator.

### `Autocorrelation of growth rates.ipynb`

**Use for:** testing whether annual or monthly shocks can be treated as independent. This matters for variance formulas and effective sample length.

### `Sigma 15 test.ipynb`

**Use for:** short-panel sigma measurement versus theoretical sigma; useful when deciding whether a 15-year panel produces biased or noisy variance estimates.

### `Variance of normal levels vs diff.ipynb`

**Use for:** methodological comparison of level volatility and difference volatility, numerical integration, Monte Carlo checks, and transformations.

---

## C. Population grouping and simulation

### `Quantile Simulations.ipynb`

**Use for:** theoretical/empirical quantiles, Pareto and lognormal tails, population counts, value-balanced groups, and size-dependent growth.

### `Experiment 3. Micro shocks. (s, gr).ipynb`

**Likely inputs:** empirical or theoretical grouped populations and microshock arrays.

**Likely outputs:** aggregate/group volatility under shock-family and shock-scale choices.

**Question to answer during inspection:** is `Nq` an effective population/concentration object, a literal group count, or a notation that changed over time?

### `Experiment 4. Micro shocks. (s, gr, size dists).ipynb`

**Use for:** full simulation grid over:
- size distributions;
- shock distributions;
- shock scales `s`;
- group/quantile constructions;
- repeated simulations.

**Search for:** `exp_var_`, `sizes`, `dist`, `s`, `Q`, `q`, `i`, period columns, seeds, and output paths.

### `Experiment 5. Simple var vs nq, s. (s).ipynb`

**Directly observed responsibilities:**
- `IMPORT == 0` export filter;
- firm-year `VART` matrix;
- size ordering;
- cumulative-value partitions;
- empirical shock dispersion;
- simulated shocks;
- `yqs_var`, `noise_var`, `base_var`, `nqs`, `q`, `s`, `m`;
- `aggregated_simulation_results.csv`.

**Main caution:** this is a generator candidate. No inspected cell maps a fitted slope to the reported alpha.

### `bkp Exp5.ipynb`

**Use only when:** the canonical Experiment 5 lacks an older `Nq` definition, output path, or figure. Treat as a historical comparison, not an equal-authority implementation.

---

## D. Variance, covariance, and local-to-global decomposition

### `Linear Base + Noise decomposition.ipynb`

**Direct role:** mechanism notebook. It creates cumulative-size partitions and decomposes group values into base, common, and noise pieces before calculating covariance structures.

**Use for current synthesis:** determine which terms add exactly and which covariance terms prevent a simple weighted average of local alphas.

### `Covariance Terms Bootstrap Experiments.ipynb`

**Direct role:** empirical partition and covariance notebook using `ID_Y.csv`.

**Search for:**
- `parts`;
- `cov_elements_desc_*`;
- `parts_cross_cov_*`;
- random versus sorted partitions;
- linear versus log variants;
- export versus import variants;
- diagonal/off-diagonal decomposition.

### `Experiment 2. Extensive BME.ipynb`

**Role:** heavier bootstrap/decomposition engine. It appears to create base, total, and covariance output families and to separate common/background/noise components.

**Use for:** reconstructing the finite-population variance formula and covariance correction, not for a first visual pass.

### `Decomposition terms. w Bootstrap.ipynb`

**Role:** high-priority historical estimator lead.

**Known only from repository notes:** CSV input, `groupby`, covariance, `polyfit`, `log10`, self-variance and `n`, boxplots, heatmaps.

**Action:** search history, backups, checkpoints, and recovered blobs by distinctive code strings—not only by filename.

### `Partial dependence Analysis.ipynb`

**Role:** likely direct bridge to the new PI hypothesis. It examines total variance as a function of population and partial derivatives under alternative distributions and sigma values.

### `Partial dependence Computation.ipynb` and `Partial dependence Computation - 2.ipynb`

**Role:** likely producers for the analysis notebook. Inspect before executing the analysis notebook so inputs and parameter grids are understood.

### `sigma vectors with uniform matrix.ipynb`

**Use for:** simplified covariance-matrix thought experiment; helpful as a control case for aggregate variance with uniform off-diagonal structure.

### `Tendency out of signal.ipynb`

**Use for:** trend/noise decompositions, OLS checks, and numerical covariance identities. Potentially useful for validating formula algebra.

---

## E. Estimator and figure production

### `Sigma vs log(n), q plots.ipynb`

**Directly observed:**
- loads `exp_var_*` families;
- creates `var_diff_qi` and `var_diff_agg_i` after bias corrections;
- constructs `n` from simulated size distributions;
- plots variance against `n` on log scales;
- overlays `1/n` references;
- writes `sigma_vs_n_grs.png`, `sigma_vs_n_szdists.png`, and related figures;
- contains bias-slope fits that are not themselves the final alpha estimate.

**This is the first figure notebook to open after reading the thesis text.**

### `Std of quantiles.ipynb`

**Use for:** locating empirical quantile-volatility figures and any summary statistic connecting bins to the whole population.

### `Growth rates vs mean divergence vs quantiles.ipynb`

**Use for:**
- well-behaved versus unstable firms;
- quantiles with few large firms;
- aggregation by sample size;
- Laplace/Subbotin alternatives;
- log-base conventions.

**Likely role:** methodological bridge between empirical microshocks and the simulation/figure notebooks.

### `Higher frequency (Fourier).ipynb`

**Use later for:** frequency decomposition and variance explained. Relevant only after the annual-frequency result is understood.

---

# 3. Upstream data-construction notebooks

These are essential when execution begins, but they should not dominate the first conceptual pass.

| Notebook | Likely role |
|---|---|
| `0.0 Extract from database.ipynb` | Large original extraction and preprocessing workflow; potential dynamic producer of analysis panels. |
| `Data sampling (old).ipynb` | Chunking, filtering, aggregation, flow selection, and reusable sampling functions. |
| `Save Growth info.ipynb` | Creates standardized size/growth panels used by downstream experiments. |
| `Firm sizes - old.ipynb` | Historical firm-size builder and saved size outputs. |
| `VFTE vs VART.ipynb` | Validates or compares border transaction-value measures. |
| `Dataset totals.ipynb` | Data sanity and distribution overview. |
| `Population evolution (violin plots).ipynb` | Firm-size evolution, entry/exit, age, and inverse age. |
| `Month distribution etc.ipynb` | Transaction frequency, active/inactive periods, and size/growth summaries. |
| `Monthly time series.ipynb` | Monthly aggregates and temporal visualizations; uses shared aggregation helpers. |
| `Product seasonality.ipynb` | Seasonal correction, wave fitting, PCA, and year-jump treatment. |

**Execution rule:** identify the authoritative producer of `ID_Y.csv` or its successor before refactoring any consumer.

---

# 4. Adjacent research fronts and reusable material

These notebooks are intellectually valuable but should remain outside active WIP until the export-alpha gate is resolved.

## Trade margins, entry, and firm dynamics

- `in-ex margins.ipynb`
- `Literal Margins.ipynb`
- `Bernard margins.ipynb`
- `Population evolution (violin plots).ipynb`
- `Month distribution etc.ipynb`

**Potential paper family:** entry/exit, intensive/extensive margins, frequency, and growth heterogeneity.

## Sourcing, products, and diversification

- `Sourcing strategies.ipynb`
- `RC Analisys of fixed effects..ipynb`
- `Revealed competitiveness (weighted means).ipynb`
- `Countries revealed competitiveness.ipynb`
- `Firm baskets CN 4-digit.ipynb`
- `Firm basket networks.ipynb`
- `Determinants of diversification_2.ipynb`
- `Krammarx regression. Product nw, etc..ipynb`
- `Product concordance.ipynb`

**Potential paper family:** firm sourcing strategies, product/country diversification, and size-conditioned network structure.

## Network and propagation experiments

- `Acemoglu Numerical Tests.ipynb`
- `Production Network tests.ipynb`
- `Input Output adjacency.ipynb`
- `Leontieff aggregation tests-Copy1.ipynb`
- `Star vs complete leontieff propagation.ipynb`
- `sigma vectors with uniform matrix.ipynb`
- `Assortativity_2.ipynb`
- `Degree distribution and assortativity. Diversity.ipynb`
- `degree data (legacy).ipynb`
- `Deegree distribution_2.ipynb`
- `Link characteristics.ipynb`

**Potential paper family:** network topology, covariance propagation, diversification, and aggregate volatility.

---

# 5. What to ignore initially

Do not begin with:

- `.ipynb_checkpoints/`;
- `notebooks/old/`;
- `recovered-blob_*.ipynb`;
- `bkp` notebooks;
- duplicate filenames in several locations;
- broad visualizations unrelated to variance scaling;
- repository-wide modernization.

Open a backup/checkpoint only when:

1. the canonical notebook is missing or corrupt;
2. a referenced output producer cannot be located;
3. a distinctive function, variable, or path exists only in the historical copy;
4. the PI recognizes the historical figure rather than the canonical one.

---

# 6. Agent search recipe

## First-pass search terms

Search notebook JSON for these exact strings:

```text
ID_Y.csv
IMPORT == 0
VART
Nq
nqs
get_n
var_diff_qi
var_diff_agg_i
yqs_var
noise_var
base_var
exp_var_
aggregated_simulation_results
sigma_vs_n
polyfit
linregress
slope
alpha
Herfindahl
parts_cross_cov
cov_elements_desc
bs_base_
bs_totl_
```

## Fast command-line search

```bash
rg -l --glob '*.ipynb' \
  'ID_Y\.csv|var_diff_qi|var_diff_agg_i|yqs_var|nqs|exp_var_|sigma_vs_n|polyfit|linregress|parts_cross_cov|cov_elements_desc' \
  notebooks/
```

Extract readable notebook source without running it:

```bash
jq -r '.cells[] | "\n### CELL \(.cell_type)\n", (.source[]? // empty)' NOTEBOOK.ipynb
```

Search only code cells:

```bash
jq -r '.cells[] | select(.cell_type == "code") | .source[]?' NOTEBOOK.ipynb \
  | rg -n 'polyfit|linregress|var_diff|cov|groupby|to_csv|savefig'
```

## Required agent output for each inspected notebook

```yaml
path:
role: GENERATOR | MOMENT_BUILDER | DECOMPOSITION | ESTIMATOR | PRESENTATION | THEORY | ADJACENT | DUPLICATE
inputs:
core_variables:
transformations:
outputs:
figures:
scientific_choices_embedded:
randomness_and_seed:
links_to_other_notebooks:
confidence: A | B | C | D
state: REVIEW
```

---

# 7. Recommended one-hour navigation pass

| Minutes | Action |
|---:|---|
| 0–5 | Read this atlas and the six estimator snippets. |
| 5–15 | Read thesis headings/equations and list the figure names or concepts that must be found. |
| 15–25 | Inspect `Test Exercise Gabaix Riccaboni` and `Gabaix Equations Review` for the early theoretical/empirical statement. |
| 25–35 | Inspect Experiment 5 and `Sigma vs log(n)` to map generator -> output -> figure. |
| 35–45 | Inspect `Linear Base + Noise`, covariance bootstrap, and Partial Dependence for the local-to-global formula. |
| 45–53 | Inspect Experiment 3/4 and upstream growth/size notebooks only for missing inputs or moments. |
| 53–58 | Build one argument table: thesis formula -> notebook -> output -> figure -> unresolved choice. |
| 58–60 | Leave one restart pointer; do not execute data or refactor code. |

---

# 8. Current highest-value questions

1. Which notebook or thesis equation defines the local alpha of a subpopulation?
2. Is the modeled object variance, standard deviation, variance of log differences, or exact nominal deviations?
3. How does each subpopulation’s size `n_k` change when total `N` changes?
4. Are the aggregate weights fixed, variance-contribution weights, or functions of `N`?
5. Which cross-covariance terms survive and how do they scale?
6. Is the whole-population alpha a constant exponent, a local elasticity, or an asymptotic dominant-component result?
7. Which existing figure most closely represents that synthesis?
8. Which output family is the authoritative source for that figure?

---

# 9. Atlas limitations

- This is a REVIEW navigation artifact, not a validated scientific dependency graph.
- Several descriptions rely on historical repository summaries and require direct notebook inspection.
- Old summaries contain factual hallucinations and unrelated interpretations; they must never be treated as primary evidence.
- Exact canonical paths for some notebooks remain to be confirmed because notebooks were moved, duplicated, checkpointed, or recovered.
- No dataset was opened and no notebook was executed to produce this atlas.

## Exact next pointer

Start with the thesis section defining the variance/population relationship, then inspect—in order—`Test Exercise Gabaix Riccaboni.ipynb`, `Experiment 5. Simple var vs nq, s. (s).ipynb`, `Sigma vs log(n), q plots.ipynb`, and the decomposition/partial-dependence notebooks. Stop when the first complete formula -> code -> output -> figure chain is documented or the first exact missing link is recorded.
