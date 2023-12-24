# %% [markdown]
# # Extract from database
# 
# This notebook contains all queries to the source database.

# %%
# %%
import pandas as pd
import dask.dataframe as dd
from dask.diagnostics import ProgressBar
from numpy import log10, arange
import matplotlib.pyplot as plt

# %% [markdown]
# General settings

# %%
drive_path = '/media/matias/Elements/export_france/data/type1/DP1610_MAASTRICHT1_1997_2013/'
save_path = './../../data/processed/'

colnames = [u'YEAR', u'MONTH', u'FLUX', u'ID', u'DEPT', u'CN ID 8', u'CPA6',
       u'PYOD', u'PAYP', u'VAT', u'PRIFAC', u'DEVFAC', u'VFTE', u'VART', u'D_MASSE', u'MASSE', u'USUP', u'USUP_MT']
colname_no = dict(zip(colnames, range(18)))

# Function to read data for specified columns and years
def get_data(columns, drive_path, start_year=1997, end_year=2014):
    df_list = []
    for y in range(start_year, end_year):
        df = dd.read_table(f'{drive_path}DP1610_MAASTRICHT1_{y}.txt', 
                           usecols=list(map(colname_no.get, columns)),
                           delimiter=';', header=None, dtype={4: 'object', 9: 'object'})
        df.columns = columns  # Assigning column names
        df_list.append(df)
    return dd.concat(df_list)


# %%


def chunk(s):
    '''
    The function applied to the
    individual partition (map)
    '''    
    return s.apply(lambda x: list(set(x)))


def agg(s):
    '''
    The function whic will aggrgate 
    the result from all the partitions(reduce)
    '''
    s = s._selected_obj    
    return s.groupby(level=list(range(s.index.nlevels))).sum()


def finalize(s):
    '''
    The optional functional that will be 
    applied to the result of the agg_tu functions
    '''
    return s.apply(lambda x: len(set(x)))

tunique = dd.Aggregation('tunique', chunk, agg,finalize)



# %% [markdown]
# ## Build datasets
# ### - Price and quantities

# %%
columns = [u'YEAR', u'MONTH', u'FLUX', u'ID', u'CN ID 8', u'PYOD', u'VART', u'MASSE', u'USUP', u'USUP_MT']


# Function to process price and quantities dataset
def process_price_quantities(columns, drive_path, end_year):
    data = get_data(columns, drive_path, end_year=end_year)
    # display(data.head())
    grouped = data[data.FLUX == 2].groupby(['ID', 'CN ID 8', 'MONTH', 'YEAR'])
    yearly_qv = grouped[['VART', 'MASSE']].sum().compute()
    yearly_qv.to_csv(f'{save_path}units_qv.csv')
    return yearly_qv

yearly_qv = process_price_quantities(columns, drive_path, end_year=2014)
print(yearly_qv.head())

# with ProgressBar():
#     yearly_details = data_.loc[data_.FLUX == 2].head(1000).groupby(['ID', 'CN ID 8', 'YEAR']).agg(
#         {'VART': sum, 'MASSE': sum, 'USUP': tunique, 'USUP': first, 'USUP_MT': sum}).compute()
# yearly_details.to_csv(save_path + 'units_detail.csv')

# %% [markdown]
# ### - Firm sizes

# %%
columns = [u'YEAR', u'MONTH', u'FLUX', u'ID', u'VAT', u'VART']
data = get_data(columns, drive_path, end_year = 1999)

data['IMPORT'] = data['FLUX'] % 2

firm_sizes = data.groupby(['ID', 'IMPORT','YEAR'])[['VART']].sum().reset_index()
buyr_sizes = data.groupby(['VAT', 'IMPORT','YEAR'])[['VART']].sum().reset_index()

with ProgressBar():
    firm_sizes = firm_sizes.compute()
    buyr_sizes = buyr_sizes.compute()
    

firm_sizes.to_csv(save_path + 'firm_sizes_99.csv', index = False)
buyr_sizes.to_csv(save_path + 'buyr_sizes_99.csv', index = False)

# %%
pd.read_csv(save_path + 'buyr_sizes_99.csv').head()

# %% [markdown]
# ### - Value of buyer-seller links

# %%
columns = [u'YEAR', u'FLUX', u'ID', u'VAT', u'VART']

data = get_data(columns, drive_path, end_year = 1999)

data['IMPORT'] = data['FLUX'] % 2

links = data.groupby(['IMPORT','YEAR','ID','VAT'])['VART'].sum().reset_index()

with ProgressBar():
    out = links.compute()
out.to_csv(save_path + 'buyer_seller_link_value.csv', index = False)

# %%
pd.read_csv(save_path + 'buyer_seller_link_value.csv').head()

# %% [markdown]
# ### - Sourcing info

# %%
# columns = [u'YEAR', u'MONTH', u'FLUX', u'ID', u'CN ID 8', 'PYOD', u'VART']

# data = get_data(columns, drive_path, end_year = 1999)

# data['IMPORT'] = data['FLUX'] % 2
# data['QUARTER'] = ((data['MONTH'] -1)// 3) + 1

# CN_full = pd.read_csv('./../../data/processed/CN_full.csv', encoding = 'utf-8')
# data = data.merge(CN_full[['CN ID 8', 'CN ID 4', 'CN label 4']])#.persist()

# # Compute and save
# sourcing_strategies = data.loc[data.IMPORT == 1].groupby(['YEAR', 'ID', 'CN ID 4', 'PYOD'])[['VART']].sum() #rm QUARTER for yearly dataset
# with ProgressBar():
#     out = sourcing_strategies.compute()
# out.to_csv(save_path + 'sourcing_strategies_99.csv')

# export_bundles = data.loc[data.IMPORT == 0].groupby(['YEAR', 'ID', 'CN ID 4', 'PYOD'])[['VART']].sum()
# with ProgressBar():
#     out2 = export_bundles.compute()
# out2.to_csv(save_path + 'export_bundles_99.csv')

# # Compute and save
# sourcing_strategies_qr = data.loc[data.IMPORT == 1].groupby(['YEAR', 'QUARTER','ID', 'CN ID 4', 'PYOD'])[['VART']].sum() #rm QUARTER for yearly dataset
# with ProgressBar():
#     out = sourcing_strategies_qr.compute()
# out.to_csv(save_path + 'sourcing_strategies_99_qr.csv')

# export_bundles_qr = data.loc[data.IMPORT == 0].groupby(['YEAR', 'QUARTER', 'ID', 'CN ID 4', 'PYOD'])[['VART']].sum()
# with ProgressBar():
#     out2 = export_bundles_qr.compute()
# out2.to_csv(save_path + 'export_bundles_99_qr.csv')

# %%
import pandas as pd
from dask.diagnostics import ProgressBar

def compute_and_save_grouped_data(data, group_cols, agg_col, save_path, file_name, extra_group_cols=None):
    if extra_group_cols is not None:
        group_cols.extend(extra_group_cols)

    grouped_data = data.groupby(group_cols)[[agg_col]].sum()
    with ProgressBar():
        output = grouped_data.compute()
    output.to_csv(f'{save_path}{file_name}.csv')
    return output

def add_import_quarter_columns(data):
    data['IMPORT'] = data['FLUX'] % 2
    data['QUARTER'] = ((data['MONTH'] - 1) // 3) + 1
    return data

# Main processing function
def process_sourcing_export(data, drive_path, end_year, save_path):
    data = get_data(columns, drive_path, end_year=end_year)
    data = add_import_quarter_columns(data)
    
    # Merging additional data
    CN_full = pd.read_csv('./../../data/processed/CN_full.csv', encoding='utf-8')
    data = data.merge(CN_full[['CN ID 8', 'CN ID 4', 'CN label 4']])
    
    # Compute and save
    compute_and_save_grouped_data(data[data.IMPORT == 1], 
                                  ['YEAR', 'ID', 'CN ID 4', 'PYOD'], 
                                  'VART', save_path, 'sourcing_strategies_99')

    compute_and_save_grouped_data(data[data.IMPORT == 0], 
                                  ['YEAR', 'ID', 'CN ID 4', 'PYOD'], 
                                  'VART', save_path, 'export_bundles_99')

    # For quarterly data
    compute_and_save_grouped_data(data[data.IMPORT == 1], 
                                  ['YEAR', 'ID', 'CN ID 4', 'PYOD'], 
                                  'VART', save_path, 'sourcing_strategies_99_qr', 
                                  extra_group_cols=['QUARTER'])

    compute_and_save_grouped_data(data[data.IMPORT == 0], 
                                  ['YEAR', 'ID', 'CN ID 4', 'PYOD'], 
                                  'VART', save_path, 'export_bundles_99_qr', 
                                  extra_group_cols=['QUARTER'])

# Usage
columns = [u'YEAR', u'MONTH', u'FLUX', u'ID', u'CN ID 8', 'PYOD', u'VART']
drive_path = # Define drive path
end_year = 1999
save_path = # Define save path

process_sourcing_export(data, drive_path, end_year, save_path)


# %%
pd.read_csv(save_path + 'export_bundles_99.csv').head()

# %% [markdown]
# ### - Bernard's margins

# %%
import pandas as pd
from dask.diagnostics import ProgressBar

# Define the columns needed
columns = [u'YEAR', u'FLUX', u'ID', u'CN ID 8', 'PYOD', u'VART', u'VAT']

# Load the data
data = get_data(columns, drive_path, end_year=1999)

# Apply transformation
data['IMPORT'] = data['FLUX'] % 2

# Group and aggregate the data
grouped = data.groupby(['IMPORT', 'YEAR', 'ID']).agg({'VAT': tunique, 'PYOD': tunique, 'CN ID 8': tunique, 'VART': 'sum'})

# Compute the results
with ProgressBar():
    result = grouped.compute()

# Save the results to CSV
result.to_csv(save_path + 'bernards_margins.csv')


# %% [markdown]
# ### - Krammar's determinants of diversification

# %%
columns = [u'YEAR', u'FLUX', u'ID', u'CN ID 8', u'VAT', u'PYOD', u'VART']

data = get_data(columns, drive_path, end_year = 1999)
data['IMPORT'] = data['FLUX'] % 2

grouped = data.groupby(['ID', 'YEAR', 'IMPORT'])

with ProgressBar():
    df = grouped.agg({'VART': 'sum', u'VAT': tunique, 'CN ID 8': tunique, u'PYOD': tunique}).compute()

df.to_csv(save_path + 'dets_of_diversification.csv')

# %%
# pd.read_csv(save_path + 'dets_of_diversification.csv').head()

# %% [markdown]
# ### - Degree distribution

# %%
import pandas as pd
from numpy import arange, log10
from dask.diagnostics import ProgressBar

# Settings
center_years = arange(1997, 2000, 2)
window = 1
gap = (window - 1) / 2
save_path = './../../data/processed/'   # Define where to save the output file


# Load data (you need to define how 'data' is loaded here)
# data = ...

ID_degree_res = []
VAT_degree_res = []

# Process ID degrees
for Yc in center_years:
    print(f"Processing ID degree for year {Yc} and window {window}")
    data_sec = data.loc[data.YEAR - Yc <= gap]
    
    grouped_ID = data_sec.groupby(['ID']).agg({'VAT': tunique, 'VART': sum})
    ID_degree = grouped_ID[['VAT']].reset_index()
    ID_degree.columns = ['ID', 'ID_degree']
    ID_degree['center_year'] = Yc
    ID_degree['window'] = window
    ID_degree['bin'] = pd.cut(log10(ID_degree['ID_degree']), bins=arange(-.49, 5.99, .25))
    
    filename_ID = f'{save_path}ID_deg_{Yc}_{window}.csv'
    with ProgressBar():
        ID_degree.compute().to_csv(filename_ID, index=False)
    print(f"Saved to {filename_ID}")
    ID_degree_res.append(ID_degree)

# Process VAT degrees
for Yc in center_years:
    print(f"Processing VAT degree for year {Yc} and window {window}")
    ID_deg = ID_degree_res[center_years.index(Yc)]
    
    sampling = ID_deg.groupby(['bin'], observed=True).apply(lambda x: x.sample(200, replace=True))
    data_sec_sample = data.loc[data.ID.isin(sampling['ID'].values)]
    
    grouped_VAT = data_sec_sample.groupby(['VAT']).agg({'ID': tunique, 'VART': sum})
    VAT_degree = grouped_VAT[['ID']].reset_index()
    VAT_degree.columns = ['VAT', 'VAT_degree']
    VAT_degree['center_year'] = Yc
    VAT_degree['window'] = window
    
    filename_VAT = f'{save_path}VAT_deg_{Yc}_{window}.csv'
    with ProgressBar():
        VAT_degree.compute().to_csv(filename_VAT, index=False)
    print(f"Saved to {filename_VAT}")
    VAT_degree_res.append(VAT_degree)


# %%
# # window = 3
# # assortativity_res = []
# ID_degree_res = []
# VAT_degree_res = []

# for window in [1]:
#     gap = (window-1)/2
#     center_years = arange(1997, 2000, 2)
#     print window

#     for Yc in center_years:
#         print Yc
#         data_sec = data.loc[data.YEAR - Yc <= gap]
# #         data_sec.groupby(['ID', 'VAT']).agg({'VART': sum })

#         data_sec_by_ID = data_sec.groupby(['ID']).agg({'VAT': tunique, 'VART': sum})

#         ID_degree = data_sec_by_ID[['VAT']].reset_index()
#         ID_degree.columns = [u'ID', u'ID_degree']
#         ID_degree['center_year'] = Yc
#         ID_degree['window'] = window
        
#         with ProgressBar():
#             ID_deg = ID_degree.compute()
#             ID_deg['bin'] = pd.cut(log10(ID_deg['ID_degree']), bins = arange(-.49, 5.99, .25))
#             ID_deg.to_csv(save_path + 'ID_deg_'+str(Yc)+'_'+str(window)+'.csv', index = False)
# #         ID_degree_res += [ID_degree]     

# #         ID_deg = pd.read_csv()
#         sampling = ID_deg.groupby(['bin'], observed = True).apply(lambda x: x.sample(200, replace = True))

#         data_sec_sample = data_sec.loc[data_sec.ID.isin(sampling['ID'].values)]
#         data_sec_by_VAT = data_sec_sample.groupby(['VAT']).agg({'ID': tunique, 'VART': sum})

#         VAT_degree = data_sec_by_VAT[['ID']].reset_index()
#         VAT_degree.columns = [u'VAT', u'VAT_degree']
#         VAT_degree['center_year'] = Yc
#         VAT_degree['window'] = window
#         VAT_degree_res += [VAT_degree]
#         with ProgressBar():
#             VAT_deg = VAT_degree.compute()
#             VAT_deg.to_csv(save_path + 'VAT_deg_'+str(Yc)+'_'+str(window)+'.csv', index = False)

# %%
# pd.read_csv(save_path + 'ID_deg_'+str(Yc)+'_'+str(window)).head()

# %%
# fig, ax = plt.subplots(1)
# df_degrees.groupby('VAT_degree_bin')['ID_degree','VAT_degree'].quantile(.25).plot(x = 'VAT_degree', y = 'ID_degree', marker = '', ax = ax)
# df_degrees.groupby('VAT_degree_bin')['ID_degree','VAT_degree'].quantile(.5).plot(x = 'VAT_degree', y = 'ID_degree', marker = '', ax = ax)
# df_degrees.groupby('VAT_degree_bin')['ID_degree','VAT_degree'].quantile(.75).plot(x = 'VAT_degree', y = 'ID_degree', marker = '', ax = ax)

# # df_degrees.groupby('ID_nunique_bin')['VAT_nunique','ID_nunique'].mean().plot(x = 'ID_nunique', y = 'VAT_nunique', marker = 'o', ax = ax)
# df_degrees.groupby('ID_nunique')['VAT_nunique'].median().plot(x = 'index', y = 'VAT_nunique', marker = '.', linewidth = 0, ax = ax)
# ax.set_xscale('log')
# ax.set_yscale('log')

# %% [markdown]
# ### - Buyers and sellers by foreign country

# %%
save_path = './../../data/processed/'   # Define where to save the output file
columns = [u'YEAR', u'FLUX', u'ID', u'PYOD', u'VART']
data = get_data(columns, drive_path, end_year = 1999)
data['IMPORT'] = data['FLUX'] % 2

data_by_dest = data.groupby(['IMPORT','YEAR','ID','PYOD'])['VART'].sum().reset_index()

result = data_by_dest.groupby(['PYOD', 'YEAR']).agg({'ID': tunique, 'VART': 'sum'})

with ProgressBar():
    out = result.compute()
    
out.to_csv(save_path + 'destination.csv')

# %% [markdown]
# ### - Size distribution of firms

# %%
import pandas as pd
import numpy as np
from dask.diagnostics import ProgressBar

# Settings
drive_path = '/media/matias/Elements/export_france/data/type1/DP1610_MAASTRICHT1_1997_2013/'  # Define the path to your data
end_year = 1999    # Define the end year for your data
save_path = './../../data/processed/'   # Define where to save the output file
n_bins = 20        # Number of bins for categorizing data

# Load and process the data
columns = ['YEAR', 'FLUX', 'ID', 'VART']
data = get_data(columns, drive_path, end_year=end_year)
data['IMPORT'] = data['FLUX'] % 2

# Group by IMPORT, YEAR, ID and sum the VART column
grouped_data = data.groupby(['IMPORT', 'YEAR', 'ID'])['VART'].sum().reset_index()

# Compute and convert to Pandas dataframe
with ProgressBar():
    filtered_data = grouped_data[grouped_data['VART'] > 0].compute()


# Calculate the median of VART for each ID and IMPORT
median_sizes = filtered_data.groupby(['ID', 'IMPORT'])['VART'].median().reset_index()

# Rename columns for clarity
median_sizes = median_sizes.rename(columns={'VART': 'exp_mma'})

# Log transform and binning
median_sizes['log_exp_mma'] = np.log10(median_sizes['exp_mma']).round(3)
cuts = pd.cut(median_sizes['log_exp_mma'], n_bins, labels=range(n_bins))
median_sizes['exp_mma_cat'] = cuts

# Save the processed data
median_sizes.to_csv(f'{save_path}sizes_index.csv', index=False)

# Now 'median_sizes' can be used similar to 'sizes_index' in your previous script


# %%
median_sizes.head()

# %% [markdown]
# # Older stuff

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import log10, arange

# Load the data and create time periods
links = pd.read_csv(save_path + 'buyer_seller_link_value.csv')
links['PERIOD'] = (links['YEAR'] - 1996) // 2

# Calculate degrees
degrees = links.groupby(['PERIOD', 'ID'])[['VAT']].nunique().rename(columns = {'VAT': 'ID_degree'})

# Log transform and binning
degrees['log_ID_degree'] = log10(degrees['ID_degree'])
degrees['bin_ID_degree'] = pd.cut(degrees['log_ID_degree'], arange(-.25, 4.5, 0.25))

# Calculate degree distribution
degree_dist = degrees.reset_index().groupby(['PERIOD', 'bin_ID_degree'])[['ID']].count()

# Visualization
fig, axs = plt.subplots(1, 2, figsize =(15, 6))
ax = axs[0]
for t in links['PERIOD'].unique():
    log10(degree_dist.loc[t]).reset_index().plot(marker='o', linewidth=0, ax=ax, mec='None')



