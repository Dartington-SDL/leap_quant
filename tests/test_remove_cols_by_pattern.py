import pandas as pd
from ..sub_func_remove_cols_by_pattern import remove_cols_by_pattern

def test_drops_correct_cols():
    # arrange
    raw_df = pd.DataFrame({
    'id': ["1", "2", "3", "4", "5"],
    'question_1': [4, 1, 10, 5, 8], 
    'question_2': [4, 8, 11, 9, 3],
    'question_3': [6, 4, 0, 7, 22],
    'agg_score_1': [20, 45, 88, 90, 12],
    'agg_score_2': [56, 55, 29, 99, 19],
    'agg_score_3': [95, 37, 4, 29, 57]
    })

    # act
    new_df = remove_cols_by_pattern(raw_df, 'question_')
    

    # assert
    expected_df = pd.DataFrame({
    'id': ["1", "2", "3", "4", "5"],
    'agg_score_1': [20, 45, 88, 90, 12],
    'agg_score_2': [56, 55, 29, 99, 19],
    'agg_score_3': [95, 37, 4, 29, 57]
    })
    

    pd.testing.assert_frame_equal(new_df, expected_df)


