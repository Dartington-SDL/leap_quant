from scipy.stats import zscore

def calc_add_zscore(df, col, name):

    df[name] = zscore(df[col])

    return df