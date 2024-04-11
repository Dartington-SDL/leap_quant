# Aggregate swemwebs score, convert to metric score and add to total column

import pandas as pd


def swemwebs_agg(df: pd.DataFrame, con_df: pd.DataFrame):
    """
    Returns the updated dataframe for the swemwebs measure with total raw score and metric total score
    The metric total score is determined from the data frame imported from swemwebs_conversion.csv

            Parameters:
                    df (dataframe): The swemwebs measure dataframe
                    con_df (dataframe): The swemwebs measure value conversion table

            Returns:
                    df (dataframe): The updated swemwebs measure dataframe
    """

    df["total_raw"] = df.iloc[:, 4:11].sum(axis=1)
    df_merged = df.merge(con_df, left_on="total_raw", right_on="raw")[["metric"]]
    df["total"] = df_merged.iloc[:, 0]
    df["total_final"] = df["total"]

    return df
