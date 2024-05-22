import plotly.graph_objects as go
import pandas as pd

def descriptives(df):
    df = df.dropna(subset=['pre_total', 'post_total'], how='any')
    des_dict = dict()
    des_dict['pre_des'] = df['pre_total'].describe()
    des_dict['post_des'] = df['post_total'].describe()
    des_dict['diff_des'] = df['diff'].describe()

    return des_dict

def descriptives_group(df, group):
    df = df.dropna(subset=[group, 'pre_total', 'post_total'], how='any')
    check = pd.notna(df[group]).sum()
    if check > 0:
        des_dict = dict()
        des_dict['pre_des'] = df.groupby(group)['pre_total'].describe(include='all')
        des_dict['post_des'] = df.groupby(group)['post_total'].describe(include='all')
        des_dict['diff_des'] = df.groupby(group)['diff'].describe(include='all')

        return des_dict
    else:
        return 'na_cat'
    
def dom_descriptives(df):
    df = df.dropna(subset=['pre_mm_score', 'post_mm_score'], how='any')
    des_dict = dict()
    des_dict['pre_des'] = df['pre_mm_score'].describe()
    des_dict['post_des'] = df['post_mm_score'].describe()
    des_dict['diff_des'] = df['diff_mm_score'].describe()

    return des_dict

def dom_descriptives_group(df, group):
    df = df.dropna(subset=[group, 'pre_mm_score', 'post_mm_score'], how='any')
    check = pd.notna(df[group]).sum()
    if check > 0:
        des_dict = dict()
        des_dict['pre_des'] = df.groupby(group)['pre_mm_score'].describe(include='all')
        des_dict['post_des'] = df.groupby(group)['post_mm_score'].describe(include='all')
        des_dict['diff_des'] = df.groupby(group)['diff_mm_score'].describe(include='all')

        return des_dict
    else:
        return 'na_cat'