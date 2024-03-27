# Function to transform a dictionary's values by a function

# Define function and inputs: keys and values
def reduce_df_dict_by_pattern(df_dict, function, pattern):
    dict_keys = df_dict.keys()
    dict_values = df_dict.values()

    # Create empty list to put dataframes into
    transformed_values = []

    for value in dict_values:
        transformed_values.append(function(value, pattern))

    transformed_dict = dict(zip(dict_keys, transformed_values))

    return transformed_dict
