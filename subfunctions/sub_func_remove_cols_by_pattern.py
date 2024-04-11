# Remove individual quesrtion response columns from the aggregated dataframes
import pandas as pd


def remove_cols_by_pattern(df: pd.DataFrame, pattern: str):
    """
    Returns dataframe without question response columns

        Parameters:
            df (dataframe): Dataframe with aggragated scores

            pattern (string): Pattern of column name to be removed

        Returns:
            df (dataframe): Dataframe without question response columns
    """
    # Create copy of original df to avoid potential bugs
    copied_df = pd.DataFrame.copy(df)
    df_without_question_cols = copied_df[
        copied_df.columns.drop(list(copied_df.filter(regex=pattern)))
    ]

    return df_without_question_cols
