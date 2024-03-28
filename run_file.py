# Top level run file
# Run the code from here

# Import the user defined functions
from functools import partial

from func_mors_dfs import create_mors_df_dict, filter_bab
from func_read_data import read_data
from func_score_agg import score_agg
from helper_functions import parse_mors_datestring, reduce_df_dict, parse_binary_to_boolean
from subfunctions.sub_func_remove_cols_by_pattern import remove_cols_by_pattern
from subfunctions.sub_func_transform_column_values import transform_column_values
import itertools
# File path and names. Names are used as keys in the data_dict
path = '/Users/ellengoddard/Desktop/working_data/'
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

# Define MORS dataset 
mors_df = data_dict['mors_table']

# Remove Baby Steps data from MORS 
mors_df_filtered = filter_bab(mors_df)

# Separate MORS into dataframes based on assessment tool 
mors_df_dict = create_mors_df_dict(mors_df_filtered)

# Combine the original data_dict with the mors_df_dict
combined_data_dict = {**data_dict, **mors_df_dict}

# Remove columns with column names of pattern "question_"
combined_dict_no_questions = reduce_df_dict(combined_data_dict, partial(remove_cols_by_pattern, pattern="question_"))

# Parse all datestrings into datetime64
column_names = ["assessment_date", "ptt_date_reached_dosage", "cos_date_reached_dosage", "bab_date_reached_dosage"]
partial_transform_column_vals = partial(transform_column_values, column_names=column_names, function=parse_mors_datestring)
combined_dict_parsed_dates = reduce_df_dict(combined_dict_no_questions, partial_transform_column_vals)

# Parse 0 and 1s into booleans
column_names = ["bab_reached_dosage_yn", "ptt_reached_dosage_yn", "cos_reached_dosage_yn", "bab_reached_dosage_yn"]
partial_transform_column_vals_bool_parse = partial(transform_column_values, column_names=column_names, function=parse_binary_to_boolean)
combined_dict_parsed_bools = reduce_df_dict(combined_dict_parsed_dates, partial_transform_column_vals_bool_parse)

print(f"Processed DataFrames: {combined_dict_parsed_bools.keys()}")