# Top level run file
# Run the code from here

# Import the user defined functions

from func_mors_dfs import create_mors_df_dict, filter_bab
from func_read_data import read_data
from func_score_agg import score_agg
from process_mors import process_mors
from process_swemwebs import process_swemwebs
from process_core_10 import process_core_10
from process_whooley import process_whooley
from process_pai import process_pai
from add_pre_post import pre_post_flag
from func_pre_post_merge import merge_pre_post
from func_zscore import calc_add_zscore
from func_describe import *
from func_add_name import add_name_col
from func_min_max_scale import min_max_scale
from func_fig_create import *
from func_rename_dosage_col import rename_dosage_col
from func_age_group import add_age_group
from func_matched_t_test import *
from func_test_output import *
import pandas as pd
import plotly.graph_objects as go

# File path and names. Names are used as keys in the data_dict
# path = "/Users/ellengoddard/Desktop/working_data/"
# path = "/Library/CloudStorage/OneDrive-SharedLibraries-WarrenHouseGroup/LEAP - Documents/30 Project Specific/SUMMATIVE/quant_analysis/working_data"
path = "/Users/seanmanzi/Documents/working_data/"
f_names = [
    "core_10_table",
    "mors_table",
    "pai_table_v2",
    "swemwebs_table",
    "whooley_table",
]
ext = ".csv"
# List of NaN indicators used on read in of data
na_list = [999, "", "Not applicable", "NULL", "Undefined", "Unknown"]

# Read in all datasets
data_dict = read_data(path, f_names, ext, na_list)

# Read in swemwebs conversion table
con_f_name = path + 'swemwebs_conversion' + ext
swemwebs_con_df = pd.read_csv(con_f_name)

# Run the sub functions to aggregate the scores for each measure
# and invert where necessary so a higher score is always better
data_dict = score_agg(data_dict, f_names, swemwebs_con_df)

# Define MORS dataset
mors_df = data_dict["mors_table"]

# Remove Baby Steps data from MORS
mors_df_filtered = filter_bab(mors_df)

# Separate MORS into dataframes based on assessment tool
mors_df_dict = create_mors_df_dict(mors_df_filtered)

processed_mors_dict = process_mors(mors_df_dict)
processed_swemwebs_df = process_swemwebs(data_dict['swemwebs_table'])
processed_core_10_df = process_core_10(data_dict['core_10_table'])
processed_whooley_df = process_whooley(data_dict['whooley_table'])
processed_pai_df = process_pai(data_dict['pai_table_v2'])

# Combine the processed dataframes into a new dictionary
combined_data_dict = {
    f_names[0]: processed_core_10_df,
    f_names[2]: processed_pai_df,
    f_names[3]: processed_swemwebs_df,
    f_names[4]: processed_whooley_df
}
combined_data_dict = {**combined_data_dict, **processed_mors_dict}

updated_keys = list(combined_data_dict.keys())
flagged_data_dict = dict()
merged_dict = dict()
# core-10 flag and merge
pre_events = ['DVE - Intake']
post_events = ['DVE - Exit']
flagged_data_dict[updated_keys[0]] = pre_post_flag(combined_data_dict[updated_keys[0]],
                                                   pre_events,
                                                   post_events)

merged_dict[updated_keys[0]] = merge_pre_post(flagged_data_dict[updated_keys[0]], 20, 0)

# PAI flag and merge
pre_events = ['BAB - Home Visit 1']
post_events = ['BAB - Antenatal Session 6']
flagged_data_dict[updated_keys[1]] = pre_post_flag(combined_data_dict[updated_keys[1]],
                                                   pre_events,
                                                   post_events)

merged_dict[updated_keys[1]] = merge_pre_post(flagged_data_dict[updated_keys[1]], 23, 0)

# Swemwebs flag and merge
pre_events = ['BAB - Home Visit 1']
post_events = ['BAB - Antenatal Session 6', 'BAB - Postnatal Session 9']
flagged_data_dict[updated_keys[2]] = pre_post_flag(combined_data_dict[updated_keys[2]],
                                                   pre_events,
                                                   post_events)

merged_dict[updated_keys[2]] = merge_pre_post(flagged_data_dict[updated_keys[2]], 22, 0)

# Whooley flag and merge
pre_events = ['BAB - Home Visit 1']
post_events = ['BAB - Antenatal Session 6', 'BAB - Postnatal Session 9']
flagged_data_dict[updated_keys[3]] = pre_post_flag(combined_data_dict[updated_keys[3]],
                                                   pre_events,
                                                   post_events)

merged_dict[updated_keys[3]] = merge_pre_post(flagged_data_dict[updated_keys[3]], 22, 0)

# COS-MORSB flag and merge
pre_events = ['COS - Session 1']
post_events = ['COS - Session 8']
flagged_data_dict[updated_keys[7]] = pre_post_flag(combined_data_dict[updated_keys[7]],
                                                   pre_events,
                                                   post_events)

merged_dict[updated_keys[7]] = merge_pre_post(flagged_data_dict[updated_keys[7]], 26, 1)

# COS-MORSC flag and merge
pre_events = ['COS - Registration','COS - Session 1']
post_events = ['COS - Session 8']
flagged_data_dict[updated_keys[6]] = pre_post_flag(combined_data_dict[updated_keys[6]],
                                                   pre_events,
                                                   post_events)

merged_dict[updated_keys[6]] = merge_pre_post(flagged_data_dict[updated_keys[6]], 26, 1)

# PTT-MORS flag and merge
pre_events = ['PTT - Session 1']
post_events = ['PTT - Session 6']
flagged_data_dict[updated_keys[5]] = pre_post_flag(combined_data_dict[updated_keys[5]],
                                                   pre_events,
                                                   post_events)

merged_dict[updated_keys[5]] = merge_pre_post(flagged_data_dict[updated_keys[5]], 26, 1)

# PRS-MORS flag and merge
pre_events = ['PRS - Initial ', 'PRS - Initial']
post_events = ['PRS - 10th Session ','PRS - 10th Session','PRS - Closing','PRS - 50th','PRS - 40th','PRS - 30th Session','PRS - 20th SessionSession','PRS - 15th Session ','PRS - 60th']
flagged_data_dict[updated_keys[4]] = pre_post_flag(combined_data_dict[updated_keys[4]],
                                                   pre_events,
                                                   post_events)

merged_dict[updated_keys[4]] = merge_pre_post(flagged_data_dict[updated_keys[4]], 26, 1)

## Add measure name flag column
merged_keys = list(merged_dict.keys())

for i in merged_keys:
    merged_dict[i] = add_name_col(merged_dict[i], i)

## Calculate z-scores
# z_dict = dict()

# target_col = 'pre_total'
# new_col_name = 'pre_z_score'

# for i in merged_keys:
#     z_dict[i] = calc_add_zscore(merged_dict[i], target_col, new_col_name)

# target_col = 'post_total'
# new_col_name = 'post_z_score'

# for i in merged_keys:
#     z_dict[i] = calc_add_zscore(merged_dict[i], target_col, new_col_name)

# for i in merged_keys:
#     z_dict[i]['diff_z_score'] = merged_dict[i]['post_z_score'] - merged_dict[i]['pre_z_score']

## min max scale of pre-post scores
min_scores_dict = {'core_10_table': 0,
                   'pai_table_v2': 21,
                   'swemwebs_table': 14,
                   'whooley_table': 0,
                   'COS - MORSB': 0,
                   'COS - MORSC': 0,
                   'PTT - MORS': 0,
                   'PRS - MORS': 0}
max_scores_dict = {'core_10_table': 40,
                   'pai_table_v2': 84,
                   'swemwebs_table': 70,
                   'whooley_table': 2,
                   'COS - MORSB': 70,
                   'COS - MORSC': 70,
                   'PTT - MORS': 70,
                   'PRS - MORS': 70}

mm_dict = dict()
target_col = 'pre_total'
new_col_name = 'pre_mm_score'

for i in merged_keys:
    mm_dict[i] = min_max_scale(merged_dict[i], min_scores_dict[i], max_scores_dict[i],target_col, new_col_name)

target_col = 'post_total'
new_col_name = 'post_mm_score'

for i in merged_keys:
    mm_dict[i] = min_max_scale(merged_dict[i], min_scores_dict[i], max_scores_dict[i],target_col, new_col_name)

for i in merged_keys:
    mm_dict[i]['diff_mm_score'] = merged_dict[i]['post_mm_score'] - merged_dict[i]['pre_mm_score']

## Rename/create dosage column for consistency
dos_col_list = ['None',
                'bab_reached_dosage_yn',
                'bab_reached_dosage_yn',
                'bab_reached_dosage_yn',
                'cos_reached_dosage_yn',
                'cos_reached_dosage_yn',
                'ptt_reached_dosage_yn',
                'ptt_reached_dosage_yn']

for i, j in zip(dos_col_list, merged_keys):
    mm_dict[j] = rename_dosage_col(mm_dict[j], i)

## Create age categories and add in new column
for i in merged_keys:
    mm_dict[i] = add_age_group(mm_dict[i])

## Domain merge and add min max scaled scores
dom_2 = ['core_10_table', 'swemwebs_table','whooley_table']
dom_3 = ['pai_table_v2', 'COS - MORSB', 'COS - MORSC', 'PTT - MORS', 'PRS - MORS']
col_names = ['leap_user_key', 'age_at_registration', 'age_group', 'ethnicity_b', 'home_language',
             'lone_parent', 'ward_name', 'imd_local_quint', 'dosage', 'pre_total',
             'post_total', 'diff', 'diff_mm_score','pre_mm_score',
             'post_mm_score', 'measure']

sub_col_dict = dict()
for i in merged_keys:
    sub_col_dict[i] = mm_dict[i].loc[:,col_names]

dom_2_df = pd.concat([sub_col_dict[dom_2[0]],sub_col_dict[dom_2[1]],
                      sub_col_dict[dom_2[2]]], axis=0)
dom_2_df.reset_index(inplace=True, drop=True)
dom_2_red_df = pd.concat([sub_col_dict[dom_2[0]],sub_col_dict[dom_2[1]]], axis=0)
dom_2_red_df.reset_index(inplace=True, drop=True)
dom_3_df = pd.concat([sub_col_dict[dom_3[0]],sub_col_dict[dom_3[1]],
                      sub_col_dict[dom_3[2]], sub_col_dict[dom_3[3]],
                      sub_col_dict[dom_3[4]]], axis=0)
dom_3_df.reset_index(inplace=True, drop=True)

dom_dict = {'dom_2': dom_2_df,
            'dom_2_red': dom_2_red_df,
            'dom_3_df': dom_3_df}
dom_keys = list(dom_dict.keys())
# dom_2_z_df = calc_add_zscore(dom_2_df,'diff_z_score','dom_diff_z_score')
# dom_2_z_df = calc_add_zscore(dom_2_df,'pre_z_score','dom_pre_z_score')
# dom_2_z_df = calc_add_zscore(dom_2_df,'post_z_score','dom_post_z_score')

# dom_3_z_df = calc_add_zscore(dom_3_df,'diff_z_score','dom_diff_z_score')
# dom_3_z_df = calc_add_zscore(dom_3_df,'pre_z_score','dom_pre_z_score')
# dom_3_z_df = calc_add_zscore(dom_3_df,'post_z_score','dom_post_z_score')

# fig = go.Figure()
# fig.add_trace(go.Box(y=dom_2_df['pre_mm_score']))
# fig.add_trace(go.Box(y=dom_2_df['post_mm_score']))
# fig.add_trace(go.Box(y=dom_2_df['diff_mm_score']))
# fig.show()

# fig_2 = go.Figure()
# fig_2.add_trace(go.Box(y=dom_3_df['pre_mm_score']))
# fig_2.add_trace(go.Box(y=dom_3_df['post_mm_score']))
# fig_2.add_trace(go.Box(y=dom_3_df['diff_mm_score']))
# fig_2.show()

# c_10 = combined_data_dict['core_10_table']
# a = c_10[c_10['leap_user_key'] == 464037]

## Calculate descriptives
### Measure level
des_dict = dict()
for i in merged_keys:
    des_dict[i] = descriptives(mm_dict[i])

des_age_dict = dict()
for i in merged_keys:
    des_age_dict[i] = descriptives_group(mm_dict[i], 'age_group')

des_ethnicity_dict = dict()
for i in merged_keys:
    des_ethnicity_dict[i] = descriptives_group(mm_dict[i], 'ethnicity_b')

des_home_lang_dict = dict()
for i in merged_keys:
    des_home_lang_dict[i] = descriptives_group(mm_dict[i], 'home_language')

des_lone_dict = dict()
for i in merged_keys:
    des_lone_dict[i] = descriptives_group(mm_dict[i], 'lone_parent')

des_dep_dict = dict()
for i in merged_keys:
    des_dep_dict[i] = descriptives_group(mm_dict[i], 'imd_local_quint')

des_dose_dict = dict()
for i in merged_keys:
    des_dose_dict[i] = descriptives_group(mm_dict[i], 'dosage')

### Domain level
dom_des_dict = dict()
for i in dom_keys:
    dom_des_dict[i] = dom_descriptives(dom_dict[i])

dom_des_age_dict = dict()
for i in dom_keys:
    dom_des_age_dict[i] = dom_descriptives_group(dom_dict[i], 'age_group')

dom_des_ethnicity_dict = dict()
for i in dom_keys:
    dom_des_ethnicity_dict[i] = dom_descriptives_group(dom_dict[i], 'ethnicity_b')

dom_des_home_lang_dict = dict()
for i in dom_keys:
    dom_des_home_lang_dict[i] = dom_descriptives_group(dom_dict[i], 'home_language')

dom_des_lone_dict = dict()
for i in dom_keys:
    dom_des_lone_dict[i] = dom_descriptives_group(dom_dict[i], 'lone_parent')

dom_des_dep_dict = dict()
for i in dom_keys:
    dom_des_dep_dict[i] = dom_descriptives_group(dom_dict[i], 'imd_local_quint')

dom_des_dose_dict = dict()
for i in dom_keys:
    dom_des_dose_dict[i] = dom_descriptives_group(dom_dict[i], 'dosage')

## box plots
### measure level
x_names = ['Pre-score','Post-score','Difference']
for i in merged_keys:
    overall_fig(mm_dict[i],x_names,'measure',i)

for i in merged_keys:
    overall_mean_fig(mm_dict[i],x_names,'measure',i)



### domain level
x_names = ['Pre-score','Post-score','Difference']
for i in dom_keys:
    overall_fig(dom_dict[i],x_names,'domain',i)

for i in dom_keys:
    overall_mean_fig(dom_dict[i],x_names,'domain',i)

for i in dom_keys:
    group_bar_fig(dom_dict[i],'age_group',x_names,'Age group','domain_group',i)

for i in dom_keys:
    group_bar_fig(dom_dict[i],'ethnicity_b',x_names,'Ethnicity','domain_group',i)

for i in dom_keys:
    group_bar_fig(dom_dict[i],'home_language',x_names,'Home language','domain_group',i)

for i in dom_keys:
    group_bar_fig(dom_dict[i],'lone_parent',x_names,'Lone parent status','domain_group',i)

for i in dom_keys:
    group_bar_fig(dom_dict[i],'imd_local_quint','Local IMD quintile',x_names,'domain_group',i)

for i in dom_keys:
    group_bar_fig(dom_dict[i],'dosage',x_names,'Dosage reached status','domain_group',i)

## Perform matched t-tests
## Measure level
test_dict = dict()
for i in merged_keys:
    test_dict[i] = matched_t_test(mm_dict[i])
## Domain level
dom_test_dict = dict()
for i in dom_keys:
    dom_test_dict[i] = matched_t_test(dom_dict[i])
## Measure level grouped
test_age_group_dict = dict()
for i in merged_keys:
    test_age_group_dict[i] = matched_t_test_grouped(mm_dict[i],'age_group')

test_eth_group_dict = dict()
for i in merged_keys:
    test_eth_group_dict[i] = matched_t_test_grouped(mm_dict[i],'ethnicity_b')

test_lang_group_dict = dict()
for i in merged_keys:
    test_lang_group_dict[i] = matched_t_test_grouped(mm_dict[i],'home_language')

test_lone_group_dict = dict()
for i in merged_keys:
    test_lone_group_dict[i] = matched_t_test_grouped(mm_dict[i],'lone_parent')

test_imd_group_dict = dict()
for i in merged_keys:
    test_imd_group_dict[i] = matched_t_test_grouped(mm_dict[i],'imd_local_quint')

test_dose_group_dict = dict()
for i in merged_keys:
    test_dose_group_dict[i] = matched_t_test_grouped(mm_dict[i],'dosage')

## Domain level grouped
dom_test_age_group_dict = dict()
for i in dom_keys:
    dom_test_age_group_dict[i] = matched_t_test_grouped(dom_dict[i],'age_group')

dom_test_eth_group_dict = dict()
for i in dom_keys:
    dom_test_eth_group_dict[i] = matched_t_test_grouped(dom_dict[i],'ethnicity_b')

dom_test_lang_group_dict = dict()
for i in dom_keys:
    dom_test_lang_group_dict[i] = matched_t_test_grouped(dom_dict[i],'home_language')

dom_test_lone_group_dict = dict()
for i in dom_keys:
    dom_test_lone_group_dict[i] = matched_t_test_grouped(dom_dict[i],'lone_parent')

dom_test_imd_group_dict = dict()
for i in dom_keys:
    dom_test_imd_group_dict[i] = matched_t_test_grouped(dom_dict[i],'imd_local_quint')

dom_test_dose_group_dict = dict()
for i in dom_keys:
    dom_test_dose_group_dict[i] = matched_t_test_grouped(dom_dict[i],'dosage')

dom_test_age_df = pd.DataFrame(dom_test_age_group_dict['dom_2'])

## Format t-test results
col_names = ['N', 'Pre score mean (SD)', 'Post score mean (SD)', 'T-test statistic', 'P value']

## Measure level
tab_dict = dict()
for i in merged_keys:
    tab_dict[i] = test_output(des_dict[i], test_dict[i])
m_row_names = ['Core 10', 'PAI', 'SWEMWEBS', 'Whooley', 'MORS-B COS', 'MORS-C COS', 'MORS PTT', 'MORS PRS']
all_df = test_compile(tab_dict, col_names, m_row_names)

## Domain level
dom_tab_dict = dict()
for i in dom_keys:
    dom_tab_dict[i] = test_output(dom_des_dict[i], dom_test_dict[i])
dom_row_names = ['Domain 2', 'Domain 2 - alt', 'Domain 3']
dom_all_df = test_compile(dom_tab_dict, col_names, dom_row_names)
## Measure level grouped
age_tab_dict = dict()
age_keys_dict = dict()
for i in merged_keys:
    age_tab_dict[i], age_keys_dict[i] = test_output_grouped(des_age_dict[i], test_age_group_dict[i])

age_out_dict = dict()
for i in merged_keys:
    age_out_dict[i] = test_compile(age_tab_dict[i], col_names, age_keys_dict[i])

eth_tab_dict = dict()
eth_keys_dict = dict()
for i in merged_keys:
    eth_tab_dict[i], eth_keys_dict[i] = test_output_grouped(des_ethnicity_dict[i], test_eth_group_dict[i])

eth_out_dict = dict()
for i in merged_keys:
    eth_out_dict[i] = test_compile(eth_tab_dict[i], col_names, eth_keys_dict[i])

lang_tab_dict = dict()
lang_keys_dict = dict()
for i in merged_keys:
    lang_tab_dict[i], lang_keys_dict[i] = test_output_grouped(des_home_lang_dict[i], test_lang_group_dict[i])

lang_out_dict = dict()
for i in merged_keys:
    lang_out_dict[i] = test_compile(lang_tab_dict[i], col_names, lang_keys_dict[i])

lone_tab_dict = dict()
lone_keys_dict = dict()
for i in merged_keys:
    lone_tab_dict[i], lone_keys_dict[i] = test_output_grouped(des_lone_dict[i], test_lone_group_dict[i])

lone_out_dict = dict()
for i in merged_keys:
    lone_out_dict[i] = test_compile(lone_tab_dict[i], col_names, lone_keys_dict[i])

imd_tab_dict = dict()
imd_keys_dict = dict()
for i in merged_keys:
    imd_tab_dict[i], imd_keys_dict[i] = test_output_grouped(des_dep_dict[i], test_imd_group_dict[i])

imd_out_dict = dict()
for i in merged_keys:
    imd_out_dict[i] = test_compile(imd_tab_dict[i], col_names, imd_keys_dict[i])

dose_tab_dict = dict()
dose_keys_dict = dict()
for i in merged_keys:
    dose_tab_dict[i], dose_keys_dict[i] = test_output_grouped(des_dose_dict[i], test_dose_group_dict[i])

dose_out_dict = dict()
for i in merged_keys:
    dose_out_dict[i] = test_compile(dose_tab_dict[i], col_names, dose_keys_dict[i])

## Domain level grouped
dom_age_tab_dict = dict()
dom_age_keys_dict = dict()
for i in dom_keys:
    dom_age_tab_dict[i], dom_age_keys_dict[i] = test_output_grouped(dom_des_age_dict[i], dom_test_age_group_dict[i])

dom_age_out_dict = dict()
for i in dom_keys:
    dom_age_out_dict[i] = test_compile(dom_age_tab_dict[i], col_names, dom_age_keys_dict[i])

dom_eth_tab_dict = dict()
dom_eth_keys_dict = dict()
for i in dom_keys:
    dom_eth_tab_dict[i], dom_eth_keys_dict[i] = test_output_grouped(dom_des_ethnicity_dict[i], dom_test_eth_group_dict[i])

dom_eth_out_dict = dict()
for i in dom_keys:
    dom_eth_out_dict[i] = test_compile(dom_eth_tab_dict[i], col_names, dom_eth_keys_dict[i])

dom_lang_tab_dict = dict()
dom_lang_keys_dict = dict()
for i in dom_keys:
    dom_lang_tab_dict[i], dom_lang_keys_dict[i] = test_output_grouped(dom_des_home_lang_dict[i], dom_test_lang_group_dict[i])

dom_lang_out_dict = dict()
for i in dom_keys:
    dom_lang_out_dict[i] = test_compile(dom_lang_tab_dict[i], col_names, dom_lang_keys_dict[i])

dom_lone_tab_dict = dict()
dom_lone_keys_dict = dict()
for i in dom_keys:
    dom_lone_tab_dict[i], dom_lone_keys_dict[i] = test_output_grouped(dom_des_lone_dict[i], dom_test_lone_group_dict[i])

dom_lone_out_dict = dict()
for i in dom_keys:
    dom_lone_out_dict[i] = test_compile(dom_lone_tab_dict[i], col_names, dom_lone_keys_dict[i])

dom_imd_tab_dict = dict()
dom_imd_keys_dict = dict()
for i in dom_keys:
    dom_imd_tab_dict[i], dom_imd_keys_dict[i] = test_output_grouped(dom_des_dep_dict[i], dom_test_imd_group_dict[i])

dom_imd_out_dict = dict()
for i in dom_keys:
    dom_imd_out_dict[i] = test_compile(dom_imd_tab_dict[i], col_names, dom_imd_keys_dict[i])

dom_dose_tab_dict = dict()
dom_dose_keys_dict = dict()
for i in dom_keys:
    dom_dose_tab_dict[i], dom_dose_keys_dict[i] = test_output_grouped(dom_des_dose_dict[i], dom_test_dose_group_dict[i])

dom_dose_out_dict = dict()
for i in dom_keys:
    dom_dose_out_dict[i] = test_compile(dom_dose_tab_dict[i], col_names, dom_dose_keys_dict[i])

# ttest_ind(dom_dict['dom_3_df']['pre_mm_score'],
#           dom_dict['dom_3_df']['post_mm_score'],
#           nan_policy='omit')

# mors_df = combined_data_dict['core_10_table']

# # e_list = list(mors_df['event'].unique())
# # pre_events = e_list[1]
# # post_events = e_list[0]
# pre_events = ['DVE - Intake']
# post_events = ['DVE - Exit']

# pre_flag = 'pre'
# post_flag = 'post'

# pre_list = [pre_flag] * len(pre_events)
# post_list = [post_flag] * len(post_events)

# events_list = pre_events + post_events
# flag_list = pre_list + post_list

# event_flag_df = pd.DataFrame({'event': events_list,
#                               'flag': flag_list})

# mors_df.reset_index(inplace=True, drop=True)

# core_10_flag = mors_df.merge(event_flag_df, left_on = 'event', right_on = 'event')[['flag']]
# mors_df['flag'] = core_10_flag

# uni_id = mors_df['leap_user_key'].unique()

# pre_num_list = list()
# post_num_list = list()

# for i in uni_id:
#     sub = mors_df[mors_df['leap_user_key'] == i]
#     if len(sub) > 1:
#         pre_sub = sub[sub['flag'] == 'pre']
#         pre_num_list.append(len(pre_sub))
#         post_sub = sub[sub['flag'] == 'post']
#         post_num_list.append(len(post_sub))
#     else:
#         pre_num_list.append(0)
#         post_num_list.append(0)

# pre_data_list = list()
# post_data_list = list()
# for i in range(len(uni_id)):
#     if (post_num_list[i] == 1) and (pre_num_list[i] >= 1):
#         print('one ' + 'post = ' + str(post_num_list[i]) + ' pre = ' + str(pre_num_list[i]))
#         sub = mors_df[mors_df['leap_user_key'] == uni_id[i]]
#         post_sub = sub[sub['flag'] == 'post']
#         post_sub = post_sub.sort_values('assessment_date')
#         post_sub.reset_index(inplace=True, drop=True)
#         post_data_list.append(post_sub.iloc[0,:])
#         pre_sub = sub[sub['flag'] == 'pre']
#         pre_sub = pre_sub.sort_values('assessment_date')
#         pre_sub.reset_index(inplace=True, drop=True)
#         pre_ind = pre_num_list[i] - 1
#         pre_data_list.append(pre_sub.iloc[pre_ind,:])

# for i in range(len(uni_id)):
#     if (post_num_list[i] > 1) and (pre_num_list[i] == 1):
#         print('two ' + 'post = ' + str(post_num_list[i]) + ' pre = ' + str(pre_num_list[i]))
#         sub = mors_df[mors_df['leap_user_key'] == uni_id[i]]
#         post_sub = sub[sub['flag'] == 'post']
#         post_sub = post_sub.sort_values('assessment_date')
#         post_sub.reset_index(inplace=True, drop=True)
#         post_ind = post_num_list[i] - 1
#         post_data_list.append(post_sub.iloc[post_ind,:])
#         pre_sub = sub[sub['flag'] == 'pre']
#         pre_sub = pre_sub.sort_values('assessment_date')
#         pre_sub.reset_index(inplace=True, drop=True)
#         pre_data_list.append(pre_sub.iloc[0,:])

# for i in range(len(uni_id)):
#     if (post_num_list[i] > 1) and (pre_num_list[i] > 1):
#         print('three ' + 'post = ' + str(post_num_list[i]) + ' pre = ' + str(pre_num_list[i]))
#         sub = mors_df[mors_df['leap_user_key'] == uni_id[i]]
#         post_sub = sub[sub['flag'] == 'post']
#         post_sub = post_sub.sort_values('assessment_date')
#         pre_sub = sub[sub['flag'] == 'pre']
#         pre_sub = pre_sub.sort_values('assessment_date')
#         pre_sub.reset_index(inplace=True, drop=True)
#         post_sub.reset_index(inplace=True, drop=True)
#         if post_sub.loc[0,'assessment_date'] > pre_sub.loc[(pre_num_list[i]-1),'assessment_date']:
#             post_ind = post_num_list[i] - 1
#             post_data_list.append(post_sub.iloc[post_ind,:])
#             pre_ind = pre_num_list[i] - 1
#             pre_data_list.append(pre_sub.iloc[pre_ind,:])
#         else:
#             print('multiple')

# pre_data_df = pd.DataFrame(pre_data_list)
# pre_data_df.reset_index(inplace=True, drop=True)
# post_data_df = pd.DataFrame(post_data_list)
# post_data_df.reset_index(inplace=True, drop=True)


# uni_id = post_data_df['leap_user_key'].unique()
# pre_post_list = list()
# for i in range(len(uni_id)):
#     pre_sub = pre_data_df[pre_data_df['leap_user_key'] == uni_id[i]]
#     post_sub = post_data_df[post_data_df['leap_user_key'] == uni_id[i]]

#     info = post_sub.iloc[:,0:20]
#     pre_score = pre_sub.loc[:,'total_final']
#     post_score = post_sub.loc[:,'total_final']
#     pre_post = pd.concat([info, pre_score, post_score], axis=1)
#     info_cols = list(info.columns)
#     pre_post.columns = info_cols + ['pre_total', 'post_total']
#     pre_post_list.append(pre_post.iloc[0,:])

# pre_post_df = pd.DataFrame(pre_post_list)
# pre_post_df.reset_index(inplace=True, drop=True)

# pre_post_df['diff'] = pre_post_df['post_total'] - pre_post_df['pre_total']

# check = pd.DataFrame({'pre': pre_num_list, 'post': post_num_list})
# check.value_counts()
