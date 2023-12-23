Notebook: Distribution of growth rates (=random).ipynb
Response: 
This notebook is about analysing business growth and VAT rate changes, and it applies methods such as logarithms, permutation, aggregation, bins and plotting to compare growth rates between periods and in relation to different input variables. It also assesses the relationship between different descriptive variables such as numbers of IDs and VATs.

Notebook: Gabaix numerical tests.ipynb
Response: # plt.yscale('log')
# plt.xlim(.7e-2, 5e-2)
# plt.ylim(.1e-2, 3e-2)
# plt.show()

This Jupyter notebook demonstrates various data analysis techniques to analyze the effect of shocks on the levels of a time series composed of N agents and T time steps. Technologies used include log-shocks, linear shocks approximation, and the Levy distribution Central Limit theorem. Data comes from empirical and simulated datasets composed of lognormal, normal, and Pareto distributions. Key themes include the Herfindahl expression, Gabaix decay proposition, and manipulating logarithms and time series to draw conclusions from the data.

Notebook: Quantile Simulations.ipynb
Response: #     sizes = ['logn'][j]

This Jupyter notebook is focused on analyzing distribution sizes and estimating growth rates of agents within said distributions. It uses empirical and theoretical methods to calculate N value, Pareto and lognormal tails, theoretical and empirical quantiles, simulated population and total value, size distributions, and size-dependent growth rates to understand the distribution size and growth.

Notebook: Product concordance.ipynb
Response: 
This notebook uses groupings and sizing of a given data flow to observe and display percentages of varying user data. Analysis methods employed involve sorting the results in both CPA6 and HS8 for a visual representation of the data in bar chart format. The main theme of the notebook is to visualize the makeup of the user data accordingly.

Notebook: 0.0 Extract from database.ipynb
Response: # axs[1].plot(degree_dist.unstack().mean())
# degree_dist.unstack().mean().plot(marker = 'o', linewidth = 0, ax = axs[1], mec = 'None')


This Jupyter notebook provides a comprehensive process mining and data analysis for France's 1996-1998 import export database. The notebook uses query methods and various data analysis techniques for working with the information, such as grouping, aggregation, summation and averaging. It also presents comparison and analysis of product classification, total sales values per year, month and flux, locations of transactions, firm sizes, total value of buyer-seller links, sourcing strategies, Krammar's determinants of diversification, buyers & sellers by foreign country, and degree distribution of the data.

Notebook: RC Analisys of fixed effects..ipynb
Response: # for sid in sample_ids:
#     fv = firm_prod.set_index('ID').loc[sid].groupby(['YEAR', 'CN ID 4'])[['exp', 'imp']].sum().sort_index().fillna(0)
#     fv['pct'] = 100*fv.exp/(fv.exp + fv.imp)
#     fig, ax = plt.subplots(2, figsize = (10, 6))
#     fv.pct.unstack().plot.bar(ax = ax[0], stacked = True)
#     fv.pct.rolling(4).mean().unstack().plot(ax = ax[1], marker = 'o')
#     for ax in fig.axes:
#         ax.legend(loc = (1.02, .35))
#         for tick in ax.get_xticklabels():
#             tick.set_rotation(45)
	
This Jupyter notebook analyses firm source strategies in time by using numpy, matplotlib, seaborn, and pandas modules to load and analyze data on export and import quantities, percentages, and mu coefficients. It also uses the brentq function to calculate mu values, and normpdf and erf functions to plot a cumulative distribution. The key themes are analyzing the export and import of main products of large countries over time, as well as displaying sample firm source strategies in time.

Notebook: Monthly time series.ipynb
Response: # plt.savefig('./Figures/category_at_cif_avg.png')

This Jupyter Notebook contains data analysis techniques to analyze trade data of different types of exports and imports between different countries. It also contains different visualizations to show the monthly evolution of the trade and its growth. Additionally, the notebook includes several functions from the "functions.py" file such as chunk, agg and finalized which are used to aggregate the data.

Notebook: Firm baskets CN 4-digit.ipynb
Response: This Jupyter notebook uses Python language to explore trade flows data, conduct data analysis of firms’ exporter-importer status and analyze data to identify the relationship between firm size and trade value. It uses data wrangling to filter the data, merging and grouping techniques to analyze the data and plotting to visualize the analysis results.

Notebook: Save Growth info.ipynb
Response: 
This Jupyter notebook is aimed at deriving the size distribution of firms plus growth rates by organizing data frames with different variables, resetting indices, creating pairs, and aggregating information in the data frame. It implements specific functions and data analysis techniques, aiming to analyze, organize, and summarize data in a standardized format.

Notebook: recovered-blob_020.ipynb
Response:  
This notebook investigates assortativity in France's export market, focusing on different firm sizes and leveraging techniques like plotting, sampling, aggregating, and data manipulation to analyze the degree of assortativity.

Notebook: Bernard Moxnes comprobation.ipynb
Response: 
This Jupyter notebook uses data analysis techniques such as data slicing and plotting to explore two main areas; the bilateral effects of trade and firm concentration by country. Specifically, the notebook looks at Pareto fits by country, sizes of firms, and the log (1-cdf) and pareto plot for firms. Additionally, the notebook examines the Bernard margins and a logplot of a PDF.

Notebook: Literal Margins.ipynb
Response: #     df_level_g_non_gauss = df_level_g.loc[abs(df_level_g.annual_logdiff - 0.015) >= .075]
# Summary: This Jupyter notebook uses descriptive analysis, histograms, and interpolation to analyze the growth rate distributions of countries and products. It also utilizes sample data and different cut-off points to distinguish between two distributions - Gaussian and non-Gaussian. By highlighting the number of countries vs. products that change, the notebook identifies that most products continue in the same country and suggests it is easier to have countries change than products.

Notebook: Dataset totals.ipynb
Response: # df_ = df_[df_['EXPORT']==1]
# # for all values
# descriptive_stats = df_['IMPORTS'].describe()
Summary:
This Jupyter notebook encompasses topics related to the data analysis of variables, specifically their size distribution. This includes loading in a json file to clean out variables, creating dataframe using Pandas, plotting size distributions, and using the Gabaix method with descriptive statistics for creating a synthetic model. Techniques for the data analysis include scaling, slicing, and sampling, as well as using logarithmic and normal methods.

Notebook: Leontieff aggregation tests.ipynb
Response: This Jupyter notebook demonstrates the utilization of various data analysis techniques to explore the number of the coronavirus cases in the US over time, as well as examine the effects of the lockdown measures and displacement of workers on economic indicators such as GDP growth, unemployment rate and consumer spending. Exploratory data analysis, visualisation methods, multiple linear regression, and correlation plot and analysis are used for data exploration. 

Notebook: Higher frequency (Fourier).ipynb
Response: 
This Jupyter notebook is a data analysis process to analyze data such as df_m, df_y, and x. It uses numpy Fourier transform methods to compute coefficients, plot the results, and calculate the variance explained. Additionally, it has methods to set attributes on graphs and run statistical tests.

Notebook: Production Network tests.ipynb
Response: 
This notebook focuses on understanding national production and trade and explores methodologies, analysis methods, and key themes such as the decomposition of the sales vector, reduction of countries, grouping of French firms, modelling unobserved elements and internal circulation size, and using random seed and background gradient for visualizations.

Notebook: RC Analisys of fixed effects. Geo dependence.ipynb
Response: 
This Jupyter notebook is a data analysis tool for understanding the impact of Covid-19 on large French firms. It loads necessary modules, calculates firm sizes, and analyzed data from France SIREN corporation records to explore the impact of Covid-19 on firms including their geo locations. It uses data analysis techniques such as grouping and merging, and statistical methods such as calculating average values.

Notebook: Experiment 3. Micro shocks. (s, gr).ipynb
Response: # This Jupyter notebook outlines a method of analyzing the effects of various micro and macro shocks to empirical and theoretical NQs. The data analyses used include Gaussian and Laplace deviances from the mean, along with sampling from given arrays. The notebook is specifically aimed at understanding the effects of micro and macro shocks on firm market shares when provided with specific size bins.

Notebook: Leontieff aggregation tests-Copy1.ipynb
Response: ##
This Jupyter notebook analyzes a Leontieff Matrix with reshuffling firm index and aggregation techniques to understand the volatility of the economy. It applies data analysis methods such as calculating the final demand vector and variance of the elements. It includes topics such as block mass preservation and accumulator permutations and final demand overwrites.

Notebook: Growth rates.ipynb
Response: 
This Jupyter Notebook is focused on exploring the firms population, examining the growth in values of imports/exports in Mexico from 1995-2014 at a (firm, year, flow) level. It utilizes data analysis techniques such as loading the data, creating histograms, calculating mean, standard deviation, quantiles, and examining the distribution of counts and values; it makes use of modules such as seaborn and numpy to facilitate its analysis. Additionally, it takes a deep dive into the top 1% of agents taking the most value of the given distribution.

Notebook: Gabaix Equations Review.ipynb
Response: # plt.plot(x, Levy(x, c = .3, mu = 0))
# plt.plot(x, Levy2(x, c = .3, mu = -2))
# plt.show()

This Jupyter notebook uses a mock dataset to explore the relationship between the functional form of Pareto distributions, Herfindahl index, Levy distribution, and the size of the sample. Methods used include fitting Pareto distributions, exploring the dependence of Herfindahl on sample size, and constructing Levy distributions. Data analysis methods used include bootstrapping, dropping the first quantile, plotting firm level means, and examining growth rate series. Essential functions and specialized techniques include parameter estimation, fitting curves, performing log transformations, and plotting observed values.

Notebook: Sourcing strategies.ipynb
Response: This Jupyter notebook is a description of a data analysis pipeline used to analyze firm-level international sourcing patterns. It starts by importing relevant libraries and sourcing data, then arranging the data into formats suitable for analysis. It concludes by showing examples of firm sourcing strategies over time using functions such as selecting firms that import more than 10% of some product and constructing tables of minimum and maximum values.

Notebook: Autocorrelation of growth rates.ipynb
Response: 
This Jupyter Notebook performs an analysis of firm growth rates in exports and imports, as well as autocorrelation after one year and after one month. Data manipulation techniques such as index fixing and nans croping are used to produce correlation coefficients, which are then visually represented with the help of plots.

Notebook: Bernard margins.ipynb
Response: 
This Jupyter notebook provides a data analysis of the Maastricht1 data from 1997-2013 using numpy and pandas. It explores the log-growth margins and firm sizes using log10, nan, inf, and clip functions. It then sorts the data into a DataFrame and calculates the sum of VART entries.

Notebook: Log of sum of powers.ipynb
Response: 
This Jupyter Notebook explores the effect of different distributions of growth rates on the sum of 10^x for increasing N values. It uses Python and Scipy to plot such distributions and analyze the expectation of the sum. The key analytical methods used include Pareto, Lognormal and Laplace distributions. Specialized topics covered include statistical trends such as the volatility of the total sum and the consequence of fat tailed or geometric shocks applied to the data.

Notebook: Herfindahl (Nieuwerburgh).ipynb
Response: 
This Jupyter notebook is aimed at demonstrating the calculation of the Herfindahl index to measure the degree of market concentration in terms of the market being studied. The method used is to take the natural logarithm of the market size for each participating firm followed by calculating the variance of the logarithms. Finally, the calculated variance is converted to the Herfindahl index by using the exponential function.

Notebook: VFTE vs VART.ipynb
Response: # df_ = df_.groupby(['PRIFAC']).sum().reset_index()

This notebook analyzes the 'VART_sum' variable, which represents the sum of transaction values at the border, for different (firm, year, flow) entries. It uses matplotlib, seaborn, and numpy for analyzing methods, and produces visualization graphics to summarize the data. The key themes are numerical data analysis, flow-specific statistics, and insights into the distribution of transaction values.

Notebook: Determinants of diversification_2.ipynb
Response: This Jupyter notebook investigates the correlation between different factors and diversification of international buyers using scatterplots and Table 3 regressions from Krammarz (2016). It focuses on plotting the diversification of firms of different sizes, exporting different sections, and controlled by different governance structures. Special techniques used are regression analysis and data visualization, focusing on export sections, firm sizes, and governance control.

Notebook: in-ex margins.ipynb
Response: ### Summary
This notebook uses various data analysis methods to study the growth of exports and imports of French firms through extensive and intensive margins, including the creation of phase diagrams to analyze firm growth trajectories. It uses sampling techniques and column characteristics to select the firms, and then uses visualization techniques and summation methods to analyze the data.

Notebook: Linear Base + Noise decomposition.ipynb
Response: 
This Jupyter Notebook provides a method for simulating shocks and computing various covariances between the shocks. Specifically, it leverages pandas, numpy, and matplotlib to analyze data, calculate shocks, and determine the covariance terms of the off-diagonal matrices.

Notebook: Acemoglu Numerical Tests.ipynb
Response: # Ploting the figure
# fig, axs = plt.subplots(1, 1, figsize = (5, 5))
# ax = axs
# ax.plot(np.log(s/np.sum(s)), np.log(c/ct))

This Jupyter Notebook implements an unconstrained power law distribution, the creation of the adjacency matrix, different network structures, and matrix plot for the real value added by log. Uses special techniques such as the eigendecomposition, and power law to scale sales and have certain consumtion proportions. The notebook also includes annotations to the plot.

Notebook: Decomposition terms. w Bootstrap.ipynb
Response: 
This Jupyter notebook is about analyzing data from a CSV file, and using methods such as groupby, covariances, concat, polyfit, and log10 to visualize self-variance and n, quantify shocks, measure background, and calculate covariance. Furthermore, the data is visualized through boxplots and heatmaps.

Notebook: Assortativity_2.ipynb
Response: 
The purpose of this Jupyter notebook is to analyze the connectivity of buyers and sellers in a network using the degree distributions of the buyers and sellers. To do so, the notebook imports and cleans data on buyers and sellers, calculates the median degree of buyers and average degrees of sellers in different "bins" of buyers and sellers, and visualizes the data in various types of plots using Python libraries such as Pandas and Matplotlib. Analysis methods used include degree distribution analysis, data wrangling, data aggregation, and plotting. Key themes in this notebook include network visualization, data cleaning, and data analysis.

Notebook: Growth rates as shocks from mean.ipynb
Response: #     df_level_g_list.append(df_level_g)

This notebook uses data analysis methods to investigate the relationships between firm size, export status, and the log fluctuations of firm-level sales. It provides year- and quarter-level data and uses logarithmic and exponential transforms to measure cumulative nominal shrinkage/growth. It also summarizes the mean, variance, and median of company sales.

Notebook: Degree distribution and assortativity. Diversity.ipynb
Response: 
This Jupyter notebook explores the idea of diversification in the context of a power law. It uses data analysis techniques such as reading data into lists, cumulative distributions, PDFs, and assortativity, as well as visualization methods such as setting y-axis limits and using log scale axes. It also makes use of specialized techniques such as calculating the 99th percentile of the degree and calculating bins of seller size to perform summations on.

Notebook: Size distribution (legacy).ipynb
Response: 
This Jupyter notebook provides data analysis techniques and tools for understanding the size distribution of firms, the distribution among the top agents, and the CDF of counts and value. It is used to generate empirical and theoretical results in order to visualize the results with axis settings, plot functions, and tables of values.

Notebook: degree data (legacy).ipynb
Response: #    
This Jupyter notebook outlines a study of the assortativity of firms in France. The methods involve data importation, calculation of firm sizes, window calculations, and statistical analysis with the IPython display, numpy, and pandas modules. The key themes include degree calculations, binning of firms by sizes, aggregation of data by firm and sector, and data visualization.

Notebook: Tendency out of signal.ipynb
Response: 
This Jupyter notebook explores the time series decomposition analytical technique by using linear and logarithmic methods to break down a data set into its component parts with a focus on generating the mean and variance. It also examines correlations in the data, conducts an OLS regression and numerically verifies the sum of the covariances, and employs general shock and quantile shock methods.

Notebook: Data sampling (old).ipynb
Response: 
This Jupyter notebook provides functions for reading and sampling data, such as chunk filtering, time and firm-based aggregation, select imports/exports, etc. Several key themes covered include data reading, sampling, aggregation, filtering by firm size and time, and writing as a function.

Notebook: Countries revealed competitiveness.ipynb
Response: 
This notebook uses data analysis techniques, such as loading data, grouping, aggregating and plotting, to explore the sourcing strategies of firms in relation to the variations in product imports and the characteristics of products and countries. It also studies the impact of firm size on purchasing patterns and explores the differences in the preferences of firms with different sizes.

Notebook: Input Output adjacency.ipynb
Response: 
This notebook examines the evolution of global trade across firms, over time, using the Harmonized System to identify specific products. It the methodologies used involve data cleaning and manipulation as well as numerous visualization techniques including matplotlib for plotting histogram and pdf distributions. It also applies functions such as transforming numerical data to logarithmic scale and calculating sums and averages for analysis. 

Notebook: Experiment 2. Extensive BME.ipynb
Response: 
This notebook explains how to bootstrap time series quantiles, estimate noise and factor effects on individual and sector level to characterize the cross-covariance between components, in order to disentangle noise from factor effects. The methodologies used include importing and reading data from CSVs, sampling and sorting, cutting data, grouping data, saving data, then using it to estimate and calculate noise, multivariable decomposition for a non-anonymous function, calculating and saving observed cross covariance of parts, and finally creating and characterizing diagonal and offdiagonal components for all 3x3 cross components.

Notebook: Experiment 4. Micro shocks. (s, gr, size dists).ipynb
Response: 
This Jupyter notebook studies the price and quantity dynamics of international trade with a focus on the size distributions of importing firms in France. It begins by fitting lognormal and pareto distributions to the size of imported firms, computes theoretical quantiles, and then running a variety of experiments with gaussian and laplace deviations from the mean. Finally, the notebook plots fitted distributions and convergence of mean and variance.

Notebook: Firm sizes - old.ipynb
Response: Summary: This notebook is used for analyzing firm sizes in the French economy from 1997 to 2005 with data from the DEPT, CN ID 8, PYOD, PAYP, VAT, PRIFAC, DEVFAC, VFTE, VART, D_MASSE, MASSE, USUP and USUP_MT variables. It imports modules, arranges the data, adds import and quarter columns, computes and saves firm sizes, reads into df, calculates percentage and calculates yearly, quarterly and groupby applicable values.

Notebook: sigma vectors with uniform matrix.ipynb
Response: 
This Jupyter notebook explores the sum of a symmetric matrix with values given by a uniform distribution outside the diagonal and ones on the diagonal. The expectation is always zero, and the analysis Techniques used focused on exploring the variance of the result according to the sigmas used. Data analysis was done using Pandas DataFrames and Numpy.

Notebook: Deegree distribution_2.ipynb
Response: 
This Jupyter notebook explores degree distributions in a specific network structure using visualization methods such as histograms and scatter plots. The data analysis techniques involve the use of cumulative normalization and different window sizes. It also highlights methods for processing datasets and preparing the necessary visualizations.

Notebook: Xcp by firm size barplots.ipynb
Response: # plt.close()

This Jupyter notebook summarizes trade data from the FCPY.csv file, found in the data/processed folder, and provides a graphical depiction of the sum and count of firms involved in imports and exports for a particular period. It makes use of data analysis methods such as pandas.read_csv(), groupby(), sort_index(), and unstack(), and also applies specialized techniques such as mapping LU and BE to XU and using only those countries for the sum and count of firms involved in imports and exports.

Notebook: Sigma 15 test.ipynb
Response: 
This Jupyter notebook is focused on the comparison between the short period sigma measurement of a system and its theoretical sigma. It uses Python's matplotlib library to plot the data, and employs statistical methods such as the uncertainties package and correlation analyses to compare and contrast the values. The main theme of the notebook is to understand how short period measurements can accurately reflect theoretical values.

Notebook: Variance of normal levels vs diff.ipynb
Response: 
This Jupyter notebook covers a comparison between the volatilities of Gaussians and the volatilities of their differences. The analysis utilizes multiple methods such as numerical integration, random sampling, and Monte-Carlo simulation. Furthermore, topics such as probability density functions, compression rates, and correlation of difference series are discussed and examined.

Notebook: Product seasonality.ipynb
Response: This Jupyter notebook demonstrates techniques for analyzing seasonal patterns in datasets, such as removing seasonality, fitting waves, and using principal component analysis. It also provides methods for de-emphasizing year jumps by subtracting the year mean rather than a rolling mean.

Notebook: Harmonize and compare atlas data.ipynb
Response: ## Explore functional relationships between EUR/USD, CID data, and French customs

This Jupyter notebook examines the distribution of Euros to US Dollars, the approximate median, and sample values. It uses data from CID Atlas and French customs to explore functional relationships between the currencies. It analyzes the data to identify trends and patterns in the exchange rate ratios.

Notebook: Count buyer-seller links.ipynb
Response: 
This Jupyter notebook uses importance modules such as Pandas, Matplotlib, and Dask Dataframe to analyze buyer-seller links and analyze data from a given path. It applies techniques such as chunking, aggrigation, and finalization, and creates a buyer_sizes csv with keys VAT and YEAR and the sum of the VART_sum values.

Notebook: Link characteristics.ipynb
Response: 
This Jupyter notebook evaluates the effects of various characteristics of buyer-seller pairs on the total value of transactions between them. It imports necessary modules and datasets and then employs pandas dataframe manipulation, categorical data binning, and mean regression analysis to generate a summary table and visualize patterns in the data.

Notebook: Devs vs diffs scheme.ipynb
Response: This Jupyter Notebook aims to use the diff function to compare two versions of a text. Methodologies used include running the difflib.ndiff() function to generate the diff output, exploring different attributes of the diff output, and applying the difflib.context_diff() function to generate a comparison between two versions of a text. The key theme of this notebook is highlighting the ways in which the diff function can be leveraged to compare two texts and highlight the differences between them.

Notebook: Growth rates vs mean divergence vs quantiles.ipynb
Response: 
This notebook explores methods for determining which firms demonstrate "well behaved," versus "bad behaved" behavior, using measures of deviations from mean levels, as well as analyzing growth rates for imports and exports for different aggregate sample sizes. It also examines methods for aggregating data points of specified firm sizes, the use of logs (LOG10 vs LN) for the horizontal scale in analysis as well as alternatives to calculate the true curve (Laplace, Subbotin, etc.) using quantiles with few, large firms.

Notebook: Parabolas. Simulated distribution and growth.ipynb
Response: 
This Jupyter notebook examines the total size distribution and fitting of parabolas of the value distribution of firms, and the resulting probilities, cumulative counts and quantiles. Additionally, empirical growth rate distributions, percentage changes, one-step and two-step growth simulations, and growth rate distinctions between small and large firms are explored. Specialized data analysis techniques used to generate these results include applying the logarithm to fit parabolas, using the Gaussian function to plot, quantiles to add vertical lines, and the log difference to calculate growth rates.

Notebook: Krammarx regression. Product nw, etc..ipynb
Response: 
This Jupyter notebook provides analysis on data from a dataset containing exports from several countries. It utilizes Python's sys, pd, seaborn and networkx libraries to analyse the data and generate binned plots. Key themes of the Notebook include data wrangling, data visualization, log analysis and analysis of exporter-importer relationships.

Notebook: Population evolution (violin plots).ipynb
Response: 
Summary: The purpose of this Notebook is to analyze the export and import dynamics over time, based on the sum of transaction values at the border. It loads data at (firm, year and flow) level and visualizes the distribution of firm sizes for exports/imports over time. It also examines firm entry and exit dynamics by calculating 'age' and inverse age of firms. Specialized analysis techniques include firm_mx_y and firm_stats.

Notebook: Month distribution etc.ipynb
Response: 
This Jupyter notebook examines data exported from the EU trade database in order to analyze firm size distribution, frequency of transactions, growth rates, and periods of activity and inactivity. It utilizes pandas and matplotlib functions to analyze the data and visualize the results.

Notebook: Test Exercise Gabaix Riccaboni.ipynb
Response: 
This Jupyter notebook uses data pre processing, descriptive data analysis, hypothesis testing, linear regression, and bootstrapping to explore the size distribution (Pareto) of imports and exports, along with the comovement and residual variance of each quantile. The key themes introduced are the effect of dataset size on the Herfindahl index and the estimation of log variance of parts for each log change in the size of the dataset.

Notebook: firm names.ipynb
Response: 
This Jupyter notebook is an analysis of firms population and trade flows by loading and manipulating data from multiple files. It covers specialized topics such as aggregating datasets, joining firms names, and identifying Combined Nomenclature (CN) & CPA activity codes. It then utilizes data analysis techniques such as creating a sample of the loaded dataset, filtering the dataset for years, and reading from single files.

Notebook: Revealed competitiveness (weighted means).ipynb
Response: # pct_helper(601, sample_ids)

This Jupyter Notebook is focused on analyzing the supplier network of firms by utilizing data directly imported from a CSV file to calculate firm country fixed effects as well as firm fixed effects and then analyze the sources of the firms using various techniques such as matplotlib and seaborn. Further detail was given to the effects of firm sizes in this analysis, as well as providing visuals to capture the differences in sourcing strategies over time.

Notebook: Star vs complete leontieff propagation.ipynb
Response: # 

This Jupyter notebook summarizes the methods used to analyze the value added by a power law distribution, using python scripts to produce a sample size of data, create base levels of consumption, add fluctuations to the graph, and analyze the variance of the rows and covariance of the consumption matrix to discover the aggregate volatility from the Leontieff matrix. It also explores the difference between the star network and the linear one produced by the power law distribution.

Notebook: Partial dependence Analysis.ipynb
Response: #         sim_q_size_gaus = np.power(10, q_size + np.random.normal(0, np.sqrt(var), M)/np.sqrt(2))
#         sim_q_size_mean = np.power(10, q_size)

This Jupyter notebook analyses a dataset composed of multiple CSV files and uses pandas for data cleaning, data aggregation, and exploratory data analysis. The notebook evaluates a linear dependence of the total variance with respect to population size, as well as research on the partial derivative of total variance with respect to population size when different distributions (Gaussian and Laplace) and sigma values are applied. It uses scatter plots to demonstrate the dependence of variance and partial derivative on population size and discusses the results.

Notebook: Experiment 5. Simple var vs nq, s. (s).ipynb
Response: # This Jupyter notebook primarily examines the job market for different roles and focuses on calculating an effective number called Nq. It utilizes data analysis techniques such as pareto distribution, lognormal-clipping, and bootstrapping to calculate this value. Additionally, it compares theoretical to empirical results, using statistical functions such as PPF and median-aggregates.

Notebook: Firm basket networks.ipynb
Response: 
This Jupyter notebook focuses on firm level co-export and co-import analysis, using methods such as data preparation, pruning, network functions, and exports. A wide range of techniques are explored, such as loading data, filtering, plotting, degree sequences, group comparison, country benchmarks, and log transformation. The summary is visualized with a color reference system and label information.

