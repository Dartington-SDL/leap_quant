# Aggregate Mors score and add to total column

import pandas as pd

def mors_agg(df):
    '''
    Returns the updated dataframe for the MORS measure with warmth and invasion total scores,
    inverted invasion total score and an overall total score (warmth + inverted invasion)

            Parameters:
                    df (dataframe): The MORS measure dataframe

            Returns:
                    df (dataframe): The updated MORS measure dataframe
    '''
    warmth_cols = [4,6,8,10,12,14,16]
    warmth_tot = df.iloc[:,warmth_cols].sum(axis=1)
    invas_cols = [5,7,9,11,13,15,17]
    invas_tot = df.iloc[:,invas_cols].sum(axis=1)
    df['warmth_total'] = df.iloc[:,18].combine_first(warmth_tot)
    df['invasion_total'] = df.iloc[:,19].combine_first(invas_tot)
    df['invasion_final'] = 35 - df['invasion_total']
    df['warmth_final'] = df['warmth_total']
    df['total_final'] = df['warmth_final'] + df['invasion_final']
    return df