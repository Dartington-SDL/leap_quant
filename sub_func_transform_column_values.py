import pandas as pd
def transform_column_values(df: pd.DataFrame, column_names: list[str], function: callable) -> pd.DataFrame :

    copied_df = pd.DataFrame.copy(df)
    for column_name in column_names:

        copied_df[column_name] = copied_df[column_name].apply(function)

    return copied_df
        