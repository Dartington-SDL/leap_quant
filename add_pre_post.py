import pandas as pd

def pre_post_flag(df: pd.DataFrame, pre_events, post_events):
    pre_flag = 'pre'
    post_flag = 'post'

    pre_list = [pre_flag] * len(pre_events)
    post_list = [post_flag] * len(post_events)

    events_list = pre_events + post_events
    flag_list = pre_list + post_list

    event_flag_df = pd.DataFrame({'event': events_list,
                              'flag': flag_list})
    
    df.reset_index(inplace=True, drop=True)

    df_flag = df.merge(event_flag_df, left_on = 'event', right_on = 'event')[['flag']]
    df['flag'] = df_flag

    return df

