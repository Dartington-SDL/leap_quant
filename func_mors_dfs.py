from pandas import DataFrame


# Filter and remove Baby Steps rows from MORS dataset
def filter_bab(mors_df: DataFrame) -> DataFrame:
    """
    Returns the MORS dataset without Baby Steps rows

            Parameters:
                    df (dataframe): MORS dataset

            Returns:
                    df (dataframe): filtered MORS dataset without Baby Steps rows
    """
    mors_df_filtered = mors_df.loc[mors_df["assessment_tool"] != "BAB - MORS"]
    return mors_df_filtered


# Split MORS into PRS, PTT, and COS dataframes
def create_mors_df_dict(mors_df_filtered: DataFrame) -> dict[str, DataFrame]:
    """
    Returns a dictionary of dataframes for each measure in the MORS dataset (PRS, PTT, COS-B, COS-C)
            Parameters:
                    df (dataframe): filtered MORS dataset

            Returns:
                    dict (dictionary): dataframes for PRS, PTT, COS-B, COS-C
    """
    # Initialise the dictionary
    mors_df_dict = {}

    assessment_tools = mors_df_filtered["assessment_tool"].unique()

    for tool in assessment_tools:
        filtered_df = mors_df_filtered[mors_df_filtered["assessment_tool"] == tool]
        # Update the dictionary:
        mors_df_dict[tool] = filtered_df

    return mors_df_dict


# Merge COSB and COSC if needed
