# Function to read in data into a dictionary

import pandas as pd

def read_data(path, f_names, ext, na_list):
    data_dict = dict()
    for i in f_names:
        f_in = path + i + ext
        data_dict[i] = pd.read_csv(f_in, na_values=na_list)
    
    return data_dict
