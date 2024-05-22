import plotly.graph_objects as go
from scipy.stats import sem

def overall_fig(df, x_names, folder, f_name):
    df = df.dropna(subset=['pre_mm_score', 'post_mm_score'], how='any')
    fig = go.Figure()
    fig.add_trace(go.Box(y=df['pre_mm_score'],
                         name=x_names[0],
                         boxmean='sd'))
    fig.add_trace(go.Box(y=df['post_mm_score'],
                         name=x_names[1],
                         boxmean='sd'))
    fig.add_trace(go.Box(y=df['diff_mm_score'],
                         name=x_names[2],
                         boxmean='sd'))
    fig.update_layout(yaxis_title='Scaled score',
                      title_text=f_name)
    f_path = "figures/overall/" + folder + "/" + f_name + ".png"
    #fig.write_image(f_path)
    fig.show()

def overall_mean_fig(df, x_names, folder, f_name):
    df = df.dropna(subset=['pre_mm_score', 'post_mm_score'], how='any')
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x = [1,2],
        y = [df['pre_mm_score'].mean(),df['post_mm_score'].mean()],
        error_y=dict(
            type='data',
            array=[sem(df['pre_mm_score'], nan_policy='omit'),
                   sem(df['post_mm_score'], nan_policy='omit')],
            visible=True
        )
    ))
    fig.update_layout(xaxis=dict(
        tickmode='array',
        tickvals=[1,2],
        ticktext=[x_names[0],x_names[1]])
        )
    fig.update_layout(yaxis_title='Mean scaled score',
                      title_text=f_name)
    f_path = "figures/overall/" + folder + "/" + f_name + ".png"
    #fig.write_image(f_path)
    fig.show()

def std_error_pre(df):
    if len(df) > 0:
        out = df.std() / len(df) ** 0.5
    else:
        out = 0

    return out

def std_error_post(df):
    if len(df) > 0:
        out = df.std() / len(df) ** 0.5
    else:
        out = 0

    return out

def group_bar_fig(df, group, x_names, x_lab, folder, f_name):
    df = df.dropna(subset=[group, 'pre_mm_score', 'post_mm_score'], how='any')
    pre_means = df.groupby(group)['pre_mm_score'].mean()
    post_means = df.groupby(group)['post_mm_score'].mean()
    pre_sems = df.groupby(group)['pre_mm_score'].apply(std_error_pre)
    post_sems = df.groupby(group)['post_mm_score'].apply(std_error_post)
    group_names = list(pre_means.index)
    fig = go.Figure()
    fig.add_trace(go.Bar(name=x_names[0], x=group_names, y=pre_means,
                         error_y=dict(
                            type='data',
                            array=pre_sems,
                            visible=True)
                            ))
    fig.add_trace(go.Bar(name=x_names[1], x=group_names, y=post_means,
                         error_y=dict(
                            type='data',
                            array=post_sems,
                            visible=True)
                            ))
    fig.update_layout(xaxis_title=x_lab,
                      yaxis_title='Mean scaled score')
    fig.show()