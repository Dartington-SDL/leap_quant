from functools import partial

import pandas as pd

from helper_functions import (
    categorise_columns,
    drop_columns,
    parse_binary_to_boolean,
    parse_float_to_int,
    parse_mors_datestring,
    reduce_df_dict,
    replace_negative_values_with_nan,
)
from subfunctions.sub_func_remove_cols_by_pattern import remove_cols_by_pattern
from subfunctions.sub_func_transform_column_values import transform_column_values

def process_pai(df_orig: pd.DataFrame) -> dict:
    df_orig_copy = df_orig.copy()

    # Remove columns with names of pattern "question_"
    df_no_questions = remove_cols_by_pattern(df_orig_copy ,pattern="question_")

    # Parse all datestrings into datetime64
    column_names = [
        "assessment_date",
        "bab_date_reached_dosage",
    ]

    df_parsed_dates = transform_column_values(df_no_questions, column_names,
                                              parse_mors_datestring)

    # Parse 0 and 1s into booleans
    column_names = [
        "bab_reached_dosage_yn",
        "user_has_pre_and_post"
    ]

    df_parsed_bools = transform_column_values(df_parsed_dates,column_names,
                                              parse_binary_to_boolean)

    # Change column datatype from object to categorical
    category_cols = [
        "assessment_tool",
        "event",
        "ethnicity_b",
        "home_language",
        "lone_parent",
        "lsoacode",
        "ward_name",
        "ward_code",
        "borough",
        "lsoaname",
        "mergestatus",
    ]

    df_categoricals = categorise_columns(df_parsed_bools, column_names)

    # Change column datatype from float to integer
    integer_cols = [
        "age_at_registration",
        "total",
        "total_final",
    ]

    df_parsed_floats = transform_column_values(df_categoricals, integer_cols,
                                               parse_float_to_int)

    # Replace negative ages in registration with NaN

    df_removed_negatives = replace_negative_values_with_nan(df_parsed_floats,
                                                            ["age_at_registration"])

    return df_removed_negatives