import pandas as pd

def add_sig_indicator(val):
    if (val <= 0.05) & (val > 0.01):
        val_str = '{:.3g}*'.format(val)
    elif (val <= 0.01) & (val > 0.001):
        val_str = '{:.3g}**'.format(val)
    elif val <= 0.001:
        val_str = '{:.3g}***'.format(val)
    else:
        val_str = '{:.3g}'.format(val)
    return(val_str)

def test_output(dict_des, dict_test):
    n = dict_des['pre_des']['count']
    pre_m = dict_des['pre_des']['mean']
    pre_sd = dict_des['pre_des']['std']
    post_m = dict_des['post_des']['mean']
    post_sd = dict_des['post_des']['std']

    test_list = list(dict_test)
    t_stat = test_list[0]
    p_stat = test_list[1]

    n = '{:.0f}'.format(n)
    pre_m_sd = '{:.2f} ({:.2f})'.format(pre_m,pre_sd)
    post_m_sd = '{:.2f} ({:.2f})'.format(post_m,post_sd)
    t_stat = '{:.3f}'.format(t_stat)
    p_stat = add_sig_indicator(p_stat)
    out_list = [n,
                pre_m_sd,
                post_m_sd,
                t_stat,
                p_stat]
    
    return out_list

def test_output_grouped(dict_des, dict_test):
    if dict_des != 'na_cat':
        n = list(dict_des['pre_des'].loc[:,'count'])
        pre_m = list(dict_des['pre_des'].loc[:,'mean'])
        pre_sd = list(dict_des['pre_des'].loc[:,'std'])
        post_m = list(dict_des['post_des'].loc[:,'mean'])
        post_sd = list(dict_des['post_des'].loc[:,'std'])

        group_keys = list(dict_des['pre_des'].index)
        t_stat_list = list()
        p_stat_list = list()

        for i in group_keys:
            temp_list = list(dict_test[i])
            t_stat_list.append(temp_list[0])
            p_stat_list.append(temp_list[1])
        
        n = ['{:.0f}'.format(i) for i in n]
        pre_m_sd = ['{:.2f} ({:.2f})'.format(i,j) for i,j in zip(pre_m,pre_sd)]
        post_m_sd = ['{:.2f} ({:.2f})'.format(i,j) for i,j in zip(post_m,post_sd)]
        t_stat_list = ['{:.3f}'.format(i) for i in t_stat_list]
        p_stat_list = [add_sig_indicator(i) for i in p_stat_list]
        # p_stat_str = list()
        # for i in p_stat_list:
        #     a = add_sig_indicator(i)
        #     p_stat_str.append(a)
        out_list = [n,
                    pre_m_sd,
                    post_m_sd,
                    t_stat_list,
                    p_stat_list]
        
        return out_list, group_keys
    else:
        return 'na_cat', 'na_cat'

def test_compile(dict_stats, col_names, row_names):
    if dict_stats != 'na_cat':
        tab = pd.DataFrame(dict_stats)
        tab = tab.T
        tab.columns = col_names
        tab.index = row_names

        return tab
    else:
        return 'na_cat'