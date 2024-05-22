import pandas as pd

def add_name_col(df, name):
    df['measure'] = name

    return df