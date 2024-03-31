from datetime import date, datetime
from typing import Callable, Dict, List
import numpy as np

import pandas as pd


# Helper function to iterate over dictionary of DataFrames
def reduce_df_dict(
    df_dict: Dict[str, pd.DataFrame], function: Callable[[pd.DataFrame], pd.DataFrame]
) -> Dict[str, pd.DataFrame]:
    """
    Iterates over a dictionary of DataFrames, applying a given function to each
    DataFrame.

    Parameters:
        df_dict (dict): A dictionary where keys are identifiers and values are pandas DataFrames.
        function (callable): A function that takes a DataFrame and one argument.

    Returns:
        dict: A dictionary with the same keys as `df_dict` but with the values being the transformed
              DataFrames.
    """
    # Initialize an empty dictionary for transformed DataFrames
    transformed_dict = {}

    for key, df in df_dict.items():
        # print("---")
        # print(f"\nApplying {function.func.__name__} to DataFrame '{key}':")
        # df.info()
        # Apply the function and update the transformed_dict
        transformed_dict[key] = function(df)

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


def parse_binary_to_boolean(value) -> bool | None:
    # Handle None or NaN values by directly returning None or a default value
    if pd.isnull(value):
        return None
    try:
        float_cast = float(value)
        return bool(float_cast)
    except ValueError:
        # Handle the case where conversion fails
        return None


def parse_float_to_int(value) -> int | None:
    # Handle None or NaN values by directly returning None
    if pd.isnull(value):
        return None
    try:
        # First, try to convert to float to handle string representations of floats
        float_cast = float(value)
        # Then convert the float to an integer
        int_cast = int(float_cast)
        return int_cast
    except ValueError:
        # Handle the case where conversion fails due to an invalid value (e.g., a non-numeric string)
        return None
    except TypeError:
        # Handle other types of conversion errors
        return None


def map_dataframe_dtypes(df: pd.DataFrame, dtype_map: Dict[str, str]):
    df_copy = df.copy()
    df_copy.astype(dtype_map)

    return df_copy


def categorise_columns(df: pd.DataFrame, column_names: List[str]):
    df_copy = df.copy()

    for column_name in column_names:
        df_copy[column_name] = pd.Categorical(df_copy[column_name])

    return df_copy


def drop_columns(df: pd.DataFrame, column_names: List[str]) -> pd.DataFrame:
    df_copy = df.copy()

    df_copy.drop(column_names, axis=1)

    return df_copy


def replace_negative_values_with_nan(df, column_names):
    """Replace negative values in specified columns of a DataFrame with NaN."""
    for col in column_names:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: np.nan if x < 0 else x)
    return df
