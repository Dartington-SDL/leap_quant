import pandas as pd
import logging

logger = logging.getLogger(__name__)

def transform_column_values(df: pd.DataFrame, column_names: list[str], function: callable, **kwargs) -> pd.DataFrame :

    copied_df = pd.DataFrame.copy(df)
    for column_name in column_names:
        try:
            copied_df[column_name] = copied_df[column_name].apply(function)
        except Exception:
            pass
            # name_in_kwargs = kwargs.get('name', 'Unknown')
            # logger.warning(f"Failed to apply function {function.__name__} to a value in column {column_name} in DataFrame {name_in_kwargs}. Error: {e} - is the column missing?")
        else:
            pass
            # name_in_kwargs = kwargs.get('name', 'Unknown')
            # logger.warning(f"Failed to apply function {function.__name__} to a value in column {column_name} in DataFrame {name_in_kwargs} - does a row have a blank cell?")

    return copied_df
        