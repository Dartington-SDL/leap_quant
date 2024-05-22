from sklearn.preprocessing import MinMaxScaler
import numpy as np
def min_max_scale(df, min_val, max_val, col, name):
    data = df[col]
    data = np.asarray(data)
    data = data.reshape(-1, 1)
    scaler = MinMaxScaler()
    mm_lims = np.asarray([[min_val], [max_val]])
    #mm_lims = mm_lims.reshape(1, -1)
    scaler.fit(mm_lims)
    df[name] = scaler.transform(data)

    return df