# Run individualised score aggregation and inversion functions
from typing import Dict
import pandas as pd
# Import the user defined functions
from subfunctions.sub_func_core10_agg import core10_agg
from subfunctions.sub_func_mors_agg import mors_agg
from subfunctions.sub_func_pai_agg import pai_agg
from subfunctions.sub_func_swemwebs_agg import swemwebs_agg
from subfunctions.sub_func_whooley_agg import whooley_agg

def score_agg(data_dict: Dict[str, pd.DataFrame] , f_names):
    '''
    Returns a dictionary of dataframes

            Parameters:
                    data_dict (dictionary): a dictionary of dataframes
                    f_names (list): a list of the keys for data_dict

            Returns:
                    data_dict (dictionary): updated version of data_dict with new total score columns
    '''
    data_dict[f_names[0]] = core10_agg(data_dict[f_names[0]])
    data_dict[f_names[1]] = mors_agg(data_dict[f_names[1]])
    data_dict[f_names[2]] = pai_agg(data_dict[f_names[2]])
    data_dict[f_names[3]] = swemwebs_agg(data_dict[f_names[3]])
    data_dict[f_names[4]] = whooley_agg(data_dict[f_names[4]])

    return data_dict