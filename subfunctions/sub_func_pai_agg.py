# Aggregate pai score and add to total column

import pandas as pd

def pai_agg(df: pd.DataFrame):
    '''
    Returns the updated dataframe for the PAI measure with the total score

            Parameters:
                    df (dataframe): The PAI measure dataframe

            Returns:
                    df (dataframe): The updated PAI measure dataframe
    '''
    df['total'] = df.iloc[:,4:24].sum(axis=1)
    df['total_final'] = df['total']

    return df