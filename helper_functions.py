from datetime import datetime
from datetime import date

# Helper function to iterate over dictionary of DataFrames
def reduce_df_dict(df_dict, function):
    '''
    Iterates over a dictionary of DataFrames, applying a given function to each
    DataFrame.

    Parameters:
        df_dict (dict): A dictionary where keys are identifiers and values are pandas DataFrames.
        function (callable): A function that takes a DataFrame and one argument.

    Returns:
        dict: A dictionary with the same keys as `df_dict` but with the values being the transformed
              DataFrames.
    '''
    dict_keys = df_dict.keys()
    dict_values = df_dict.values()

    # Create empty list to put dataframes into
    transformed_values = []

    for value in dict_values:
        transformed_values.append(function(value))

    transformed_dict = dict(zip(dict_keys, transformed_values))

    return transformed_dict

# Helper function to convert string into date object
# Example: "07nov2019"
def parse_mors_datestring(datestring) -> date:
    if isinstance(datestring, str):
        date_object = datetime.strptime(str(datestring), "%d%b%Y")
        return date_object
    else:
        pass


def parse_binary_to_boolean(integer) -> bool:
    float_cast = float(integer)
    boolean = bool(float_cast)
    return boolean 
