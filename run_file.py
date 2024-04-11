# Top level run file
# Run the code from here

# Import the user defined functions

from func_mors_dfs import create_mors_df_dict, filter_bab
from func_read_data import read_data
from func_score_agg import score_agg
from process_mors import process_mors

# File path and names. Names are used as keys in the data_dict
path = "/Users/ellengoddard/Desktop/working_data/"
f_names = [
    "core_10_table",
    "mors_table",
    "pai_table_v2",
    "swemwebs_table",
    "whooley_table",
]
ext = ".csv"
# List of NaN indicators used on read in of data
na_list = [999, "", "Not applicable", "NULL", "Undefined", "Unknown"]

# Read in all datasets
data_dict = read_data(path, f_names, ext, na_list)

# Run the sub functions to aggregate the scores for each measure
# and invert where necessary so a higher score is always better
data_dict = score_agg(data_dict, f_names)

# Define MORS dataset
mors_df = data_dict["mors_table"]

# Remove Baby Steps data from MORS
mors_df_filtered = filter_bab(mors_df)

# Separate MORS into dataframes based on assessment tool
mors_df_dict = create_mors_df_dict(mors_df_filtered)

processed_mors_dict = process_mors(mors_df_dict)

# Combine the original data_dict with the mors_df_dict
combined_data_dict = {**data_dict, **mors_df_dict}
