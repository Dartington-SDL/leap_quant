import pandas as pd
import numpy as np

def rename_dosage_col(df, tar_col):
    if tar_col != 'None':
        df['dosage'] = df[tar_col]
    else:
        df['dosage'] = np.nan
    
    return df