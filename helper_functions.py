from datetime import date, datetime
from typing import Callable, Dict

import pandas as pd


# Helper function to iterate over dictionary of DataFrames
def reduce_df_dict(df_dict: Dict[str, pd.DataFrame], function: Callable[[pd.DataFrame], pd.DataFrame]) -> Dict[str, pd.DataFrame]:
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


def parse_mors_datestring(datestring: str) -> date:
        """
    Helper function to convert a date string in the format "07nov2019" into a date object.

    Parameters:
        datestring (str): The date string to convert, expected to be in the format "%d%b%Y".

    Returns:
        date: A date object corresponding to the date string provided.
    """
        if isinstance(datestring, str):
            date_object = datetime.strptime(str(datestring), "%d%b%Y")
            return date_object
        else:
            pass


def parse_binary_to_boolean(integer: str | float | int) -> bool:
    """
    Converts a given input (string, float, or integer) representing a binary value into a boolean.

    Parameters:
        integer (str | float | int): The input value to convert into a boolean. Expected to represent binary (0 or 1).

    Returns:
        bool: The boolean representation of the input. Returns True for non-zero values, False otherwise.
    """
    float_cast = float(integer)
    boolean = bool(float_cast)
    return boolean
