import pandas as pd
from ..sub_func_remove_cols_by_pattern import remove_cols_by_pattern
from ..helper_functions import reduce_df_dict
import functools
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


def test_reduce_df_remove_cols():
        raw_df_1 = pd.DataFrame({
    'id': ["1", "2",],
    'question_1': [4, 1] 
        })

        raw_df_2 = pd.DataFrame({
    'id': ["3", "4",],
    'question_1': [8, 2] 
        })

        processed_df_1 =  pd.DataFrame({
    'id': ["1", "2",],
        })

        processed_df_2 =  pd.DataFrame({
    'id': ["3", "4",],
        })


        my_df_dict = {"df_1": raw_df_1, "df_2": raw_df_2}
        expected_df_dict = {"df_1": processed_df_1, "df_2": processed_df_2}

        processed_dict = reduce_df_dict(my_df_dict, functools.partial(remove_cols_by_pattern, pattern="question_"))


        pd.testing.assert_frame_equal(processed_dict["df_1"], expected_df_dict["df_1"])
        pd.testing.assert_frame_equal(processed_dict["df_2"], expected_df_dict["df_2"])


