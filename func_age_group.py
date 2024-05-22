import pandas as pd
import numpy as np

def add_age_group(df):
    min_age = 15
    max_age = 70
    # df = df[(df['age_at_registration'] >= min_age) & (df['age_at_registration'] <= max_age)]
    bins = list(range(min_age, max_age + 5, 5))
    labels = list()
    for i in bins:
        if i < max_age - 5:
            lab = str(i) + "-" + str(i+4)
            labels.append(lab)
        elif i == max_age - 5: 
            lab = str(i) + "+"
            labels.append(lab)
    
    df['age_group'] = pd.cut(df['age_at_registration'], bins, labels=labels,
                             include_lowest=True, right=False)
    df['age_group'] = df['age_group'].astype(str)
    mask = ((df['age_at_registration'] < min_age) & (df['age_at_registration'] > max_age))
    df.loc[mask, 'age_group'] = np.nan

    return df