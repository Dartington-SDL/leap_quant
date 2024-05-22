import pandas as pd

def merge_pre_post(df, max_col, mors_flag):

    uni_id = df['leap_user_key'].unique()

    pre_num_list = list()
    post_num_list = list()

    for i in uni_id:
        sub = df[df['leap_user_key'] == i]
        if len(sub) > 1:
            pre_sub = sub[sub['flag'] == 'pre']
            pre_num_list.append(len(pre_sub))
            post_sub = sub[sub['flag'] == 'post']
            post_num_list.append(len(post_sub))
        else:
            pre_num_list.append(0)
            post_num_list.append(0)

    pre_data_list = list()
    post_data_list = list()
    for i in range(len(uni_id)):
        if (post_num_list[i] == 1) and (pre_num_list[i] >= 1):
            sub = df[df['leap_user_key'] == uni_id[i]]
            post_sub = sub[sub['flag'] == 'post']
            post_sub = post_sub.sort_values('assessment_date')
            post_sub.reset_index(inplace=True, drop=True)
            post_data_list.append(post_sub.iloc[0,:])
            pre_sub = sub[sub['flag'] == 'pre']
            pre_sub = pre_sub.sort_values('assessment_date')
            pre_sub.reset_index(inplace=True, drop=True)
            pre_ind = pre_num_list[i] - 1
            pre_data_list.append(pre_sub.iloc[pre_ind,:])

    for i in range(len(uni_id)):
        if (post_num_list[i] > 1) and (pre_num_list[i] == 1):
            sub = df[df['leap_user_key'] == uni_id[i]]
            post_sub = sub[sub['flag'] == 'post']
            post_sub = post_sub.sort_values('assessment_date')
            post_sub.reset_index(inplace=True, drop=True)
            post_ind = post_num_list[i] - 1
            post_data_list.append(post_sub.iloc[post_ind,:])
            pre_sub = sub[sub['flag'] == 'pre']
            pre_sub = pre_sub.sort_values('assessment_date')
            pre_sub.reset_index(inplace=True, drop=True)
            pre_data_list.append(pre_sub.iloc[0,:])

    for i in range(len(uni_id)):
        if (post_num_list[i] > 1) and (pre_num_list[i] > 1):
            sub = df[df['leap_user_key'] == uni_id[i]]
            post_sub = sub[sub['flag'] == 'post']
            post_sub_sorted = post_sub.sort_values('assessment_date')
            pre_sub = sub[sub['flag'] == 'pre']
            pre_sub_sorted = pre_sub.sort_values('assessment_date')
            pre_sub_sorted.reset_index(inplace=True, drop=True)
            post_sub_sorted.reset_index(inplace=True, drop=True)
            if post_sub_sorted.loc[0,'assessment_date'] > pre_sub_sorted.loc[(pre_num_list[i]-1),'assessment_date']:
                post_ind = post_num_list[i] - 1
                post_data_list.append(post_sub_sorted.iloc[post_ind,:])
                pre_ind = pre_num_list[i] - 1
                pre_data_list.append(pre_sub_sorted.iloc[pre_ind,:])
            else:
                print('multiple')

    pre_data_df = pd.DataFrame(pre_data_list)
    pre_data_df.reset_index(inplace=True, drop=True)
    post_data_df = pd.DataFrame(post_data_list)
    post_data_df.reset_index(inplace=True, drop=True)


    if mors_flag == 0:
        uni_id = post_data_df['leap_user_key'].unique()
        pre_post_list = list()
        for i in range(len(uni_id)):
            pre_sub = pre_data_df[pre_data_df['leap_user_key'] == uni_id[i]]
            post_sub = post_data_df[post_data_df['leap_user_key'] == uni_id[i]]

            info = post_sub.iloc[:,0:max_col]
            pre_score = pre_sub.loc[:,'total_final']
            post_score = post_sub.loc[:,'total_final']
            pre_post = pd.concat([info, pre_score, post_score], axis=1)
            info_cols = list(info.columns)
            pre_post.columns = info_cols + ['pre_total', 'post_total']
            pre_post_list.append(pre_post.iloc[0,:])

        pre_post_df = pd.DataFrame(pre_post_list)
        pre_post_df.reset_index(inplace=True, drop=True)

        pre_post_df['diff'] = pre_post_df['post_total'] - pre_post_df['pre_total']
    elif mors_flag == 1:
        uni_id = post_data_df['leap_user_key'].unique()
        pre_post_list = list()
        for i in range(len(uni_id)):
            pre_sub = pre_data_df[pre_data_df['leap_user_key'] == uni_id[i]]
            post_sub = post_data_df[post_data_df['leap_user_key'] == uni_id[i]]

            info = post_sub.iloc[:,0:max_col]
            pre_score = pre_sub.loc[:,['invasion_final','warmth_final','total_final']]
            post_score = post_sub.loc[:,['invasion_final','warmth_final','total_final']]
            pre_post = pd.concat([info, pre_score, post_score], axis=1)
            info_cols = list(info.columns)
            pre_post.columns = info_cols + ['pre_invasion_total','pre_warmth_total','pre_total','post_invasion_total','post_warmth_total','post_total']
            pre_post_list.append(pre_post.iloc[0,:])

        pre_post_df = pd.DataFrame(pre_post_list)
        pre_post_df.reset_index(inplace=True, drop=True)

        pre_post_df['invasion_diff'] = pre_post_df['post_invasion_total'] - pre_post_df['pre_invasion_total']
        pre_post_df['warmth_diff'] = pre_post_df['post_warmth_total'] - pre_post_df['pre_warmth_total']
        pre_post_df['diff'] = pre_post_df['post_total'] - pre_post_df['pre_total']

    return pre_post_df