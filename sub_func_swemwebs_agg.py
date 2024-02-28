# Aggregate swemwebs score, convert to metric score and add to total column

import pandas as pd

def swemwebs_agg(df):
    '''
    Returns the updated dataframe for the swemwebs measure with total raw score and metric total score
    The metric total score is determined from the data frame imported from swemwebs_conversion.csv

            Parameters:
                    df (dataframe): The swemwebs measure dataframe

            Returns:
                    df (dataframe): The updated swemwebs measure dataframe
    '''
    con_df = pd.read_csv('~/Library/CloudStorage/OneDrive-SharedLibraries-WarrenHouseGroup/LEAP - Documents/30 Project Specific/SUMMATIVE/quant_analysis/working_data/swemwebs_conversion.csv')
    df['total_raw'] = df.iloc[:,4:11].sum(axis=1)
    df_merged = df.merge(con_df, left_on='total_raw', right_on='raw')[['metric']]
    df['total'] = df_merged.iloc[:,0]
    df['total_final'] = df['total']

    return df