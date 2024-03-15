# Aggregate Whooley score and add to total column

import pandas as pd

def whooley_agg(df):
    '''
    Returns the updated dataframe for the whooley measure with total score and inverted total score

            Parameters:
                    df (dataframe): The Whooley measure dataframe

            Returns:
                    df (dataframe): The updated Whooley measure dataframe
    '''
    df['total'] = df.iloc[:,4:5].sum(axis=1)
    df['total_final'] = 2 - df['total']

    return df