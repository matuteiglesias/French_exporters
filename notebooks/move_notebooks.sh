#!/bin/bash

# Move notebooks to "00_Data_Extraction_and_Preprocessing"
mv 'Count buyer-seller links.ipynb' '00_Data_Extraction_and_Preprocessing/'

# Move notebooks to "01_Exploratory_Data_Analysis"
mv 'Dataset totals.ipynb' '01_Exploratory_Data_Analysis/'
mv 'Effective diversity.ipynb' '01_Exploratory_Data_Analysis/'
mv 'Literal Margins.ipynb' '01_Exploratory_Data_Analysis/'

# Move notebooks to "02_Statistical_Analysis_and_Modeling"
mv 'Acemoglu Numerical Tests.ipynb' '02_Statistical_Analysis_and_Modeling/'
mv 'Covariance Terms Bootstrap Experiments.ipynb' '02_Statistical_Analysis_and_Modeling/'
mv 'Decomposition terms. w Bootstrap.ipynb' '02_Statistical_Analysis_and_Modeling/'
mv 'Experiment 1. Intensive. (N).ipynb' '02_Statistical_Analysis_and_Modeling/'
mv 'Experiment 2. Extensive BME.ipynb' '02_Statistical_Analysis_and_Modeling/'
mv 'Experiment 4. Micro shocks. (s, gr, size dists).ipynb' '02_Statistical_Analysis_and_Modeling/'
mv 'Experiment 5. Simple var vs nq, s. (s).ipynb' '02_Statistical_Analysis_and_Modeling/'
mv 'Gabaix Equations Review.ipynb' '02_Statistical_Analysis_and_Modeling/'
mv 'Growth rates vs mean divergence vs quantiles.ipynb' '02_Statistical_Analysis_and_Modeling/'
mv 'Linear Base + Noise decomposition.ipynb' '02_Statistical_Analysis_and_Modeling/'
mv 'Log of sum of powers.ipynb' '02_Statistical_Analysis_and_Modeling/'
mv 'Parabolas. Simulated distribution and growth.ipynb' '02_Statistical_Analysis_and_Modeling/'
mv 'Partial dependence Analysis.ipynb' '02_Statistical_Analysis_and_Modeling/'
mv 'Partial dependence Computation - 2.ipynb' '02_Statistical_Analysis_and_Modeling/'
mv 'Partial dependence Computation.ipynb' '02_Statistical_Analysis_and_Modeling/'
mv 'Variance of normal levels vs diff.ipynb' '02_Statistical_Analysis_and_Modeling/'

# Move notebooks to "03_Network_Analysis"
mv 'Deegree distribution_2.ipynb' '03_Network_Analysis/'
mv 'degree data (legacy).ipynb' '03_Network_Analysis/'
mv 'Determinants of diversification_2.ipynb' '03_Network_Analysis/'
mv 'Krammarx regression. Product nw, etc..ipynb' '03_Network_Analysis/'
mv 'Leontieff aggregation tests-Copy1.ipynb' '03_Network_Analysis/'
mv 'sigma vectors with uniform matrix.ipynb' '03_Network_Analysis/'

# Move notebooks to "04_Time_Series_Analysis"
mv 'Devs vs diffs scheme.ipynb' '04_Time_Series_Analysis/'
mv 'RC Analisys of fixed effects. Geo dependence.ipynb' '04_Time_Series_Analysis/'
mv 'RC Analisys of fixed effects..ipynb' '04_Time_Series_Analysis/'
mv 'Revealed competitiveness (weighted means).ipynb' '04_Time_Series_Analysis/'
mv 'Save Growth info.ipynb' '04_Time_Series_Analysis/'
mv 'Sourcing strategies.ipynb' '04_Time_Series_Analysis/'

# Move notebooks to "05_Economic_Insights"
mv 'in-ex margins.ipynb' '05_Economic_Insights/'
mv 'Std of quantiles.ipynb' '05_Economic_Insights/'

# Notebooks not categorized may require manual review
# mv '<Notebook_Name>.ipynb' '<Folder_Name>/'

echo "Remaining notebooks moved to respective folders."

