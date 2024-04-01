# Aggregate Core-10 score and add to total column
from pandas import DataFrame


def core10_agg(df: DataFrame) -> DataFrame:
    """
    Returns the updated dataframe for the core-10 measure with total score and inverted total score

            Parameters:
                    df (dataframe): The Core-10 measure dataframe

            Returns:
                    df (dataframe): The updated Core-10 measure dataframe
    """
    df["total"] = df["question_1"]
    df["total_final"] = 40 - df["total"]
    return df
