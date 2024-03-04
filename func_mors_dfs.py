import pandas as pd
from pandas import DataFrame

# Filter and remove Baby Steps rows from MORS dataset
def filter_bab(mors_df: DataFrame) -> DataFrame :
    mors_df_filtered = mors_df.loc[mors_df['assessment_tool'] != "BAB - MORS"] 
    return mors_df_filtered

# Split MORS into PRS, PTT, and COS dataframes
def create_mors_df_dict(mors_df: DataFrame) -> dict[str, DataFrame]:
    # Initialise the dictionary
    mors_df_dict = {}

    assessment_tools = mors_df["assessment_tool"].unique()

    for tool in assessment_tools:
        filtered_df = mors_df[mors_df['assessment_tool'] == tool]
        # Update the dictionary:
        mors_df_dict[tool] = filtered_df

    return mors_df_dict

# Merge COSB and COSC if needed
