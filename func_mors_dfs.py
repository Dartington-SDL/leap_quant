import pandas as pd
from pandas import DataFrame
from pandas import StringDtype

# Filter and remove Baby Steps rows from MORS dataset
def filter_bab(mors_df: DataFrame) -> DataFrame :
    mors_df_filtered = mors_df.loc[mors_df['assessment_tool'] != "BAB - MORS"] 
    return mors_df_filtered

# Split MORS into PRS, PTT, and COS dataframes
def mors_dfs(mors_df: DataFrame) -> dict[str, DataFrame] :
    assessment_tools = ['PRS - MORS', 'PTT - MORS', 'COS - MORS']
    mors_dfs = {assessment_tool: [mors_df['assessment_tool'] == assessment_tool] for assessment_tool in assessment_tools}
    return mors_dfs


