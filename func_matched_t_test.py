from scipy import stats

def matched_t_test(df):
    df = df.dropna(subset=['pre_mm_score', 'post_mm_score'], how='any')
    test = stats.ttest_rel(df['pre_mm_score'],
                            df['post_mm_score'],
                            nan_policy='omit')
    
    return test

def matched_t_test_grouped(df, group):
    df = df.dropna(subset=[group, 'pre_mm_score', 'post_mm_score'], how='any')
    groups = list(df[group].unique())

    test_dict = dict()
    for i in groups:
        sub_df = df[df[group] == i]

        test_dict[i] = stats.ttest_rel(sub_df['pre_mm_score'],
                                sub_df['post_mm_score'],
                                nan_policy='omit')
    
    return test_dict