# Top level run file
# Run the code from here

# Import the user defined functions
from func_read_data import read_data
from func_score_agg import score_agg

# File path and names. Names are used as keys in the data_dict
path = '~/Library/CloudStorage/OneDrive-SharedLibraries-WarrenHouseGroup/LEAP - Documents/30 Project Specific/SUMMATIVE/quant_analysis/working_data/'
f_names = ['core_10_table', 'mors_table', 'pai_table_v2',
           'swemwebs_table', 'whooley_table']
ext = '.csv'
# List of NaN indicators used on read in of data
na_list = [999, '', 'Not applicable', 'NULL', 'Undefined', 'Unknown']

# Read in all datasets
data_dict = read_data(path, f_names, ext, na_list)

# Run the sub functions to aggregate the scores for each measure
# and invert where necessary so a higher score is always better
data_dict = score_agg(data_dict, f_names)

