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


def process_mors(mors_df_dict: pd.DataFrame) -> dict:
    mors_df_dict_copy = mors_df_dict.copy()

    # Drop unnecessary dosage columns
    # NB. MORS dataset does not have dosage columns for PRS (only PTT)
    mors_df_dict_copy["PRS - MORS"] = drop_columns(
        mors_df_dict_copy["PRS - MORS"],
        ["cos_total_dosage", "cos_reached_dosage_yn", "cos_date_reached_dosage"],
    )
    mors_df_dict_copy["PTT - MORS"] = drop_columns(
        mors_df_dict_copy["PTT - MORS"],
        ["cos_total_dosage", "cos_reached_dosage_yn", "cos_date_reached_dosage"],
    )
    mors_df_dict_copy["COS - MORSB"] = drop_columns(
        mors_df_dict_copy["COS - MORSB"],
        ["ptt_total_dosage", "ptt_reached_dosage_yn", "ptt_date_reached_dosage"],
    )
    mors_df_dict_copy["COS - MORSC"] = drop_columns(
        mors_df_dict_copy["COS - MORSC"],
        ["ptt_total_dosage", "ptt_reached_dosage_yn", "ptt_date_reached_dosage"],
    )

    # Remove columns with names of pattern "question_"
    mors_dict_no_questions = reduce_df_dict(
        mors_df_dict_copy, partial(remove_cols_by_pattern, pattern="question_")
    )

    # Parse all datestrings into datetime64
    column_names = [
        "assessment_date",
        "ptt_date_reached_dosage",
        "cos_date_reached_dosage",
        "bab_date_reached_dosage",
    ]
    partial_transform_column_vals_date_parse = partial(
        transform_column_values,
        column_names=column_names,
        function=parse_mors_datestring,
    )
    mors_dict_parsed_dates = reduce_df_dict(
        mors_dict_no_questions, partial_transform_column_vals_date_parse
    )

    # Parse 0 and 1s into booleans
    column_names = [
        "bab_reached_dosage_yn",
        "ptt_reached_dosage_yn",
        "cos_reached_dosage_yn",
        "bab_reached_dosage_yn",
    ]
    partial_transform_column_vals_bool_parse = partial(
        transform_column_values,
        column_names=column_names,
        function=parse_binary_to_boolean,
    )
    mors_dict_parsed_bools = reduce_df_dict(
        mors_dict_parsed_dates, partial_transform_column_vals_bool_parse
    )

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
    partial_column_cat_changer = partial(categorise_columns, column_names=category_cols)
    mors_dict_categoricals = reduce_df_dict(
        mors_dict_parsed_bools, partial_column_cat_changer
    )

    # Change column datatype from float to integer
    integer_cols = [
        "age_at_registration",
        "warmth_total",
        "invasion_total",
        "invasion_final",
        "warmth_final",
        "total_final",
    ]
    partial_column_parse_int = partial(
        transform_column_values, column_names=integer_cols, function=parse_float_to_int
    )
    mors_dict_parsed_floats = reduce_df_dict(
        mors_dict_categoricals, partial_column_parse_int
    )

    # Replace negative ages in registration with NaN
    partial_replace_negatives = partial(
        replace_negative_values_with_nan, column_names=["age_at_registration"]
    )
    mors_dict_removed_negatives = reduce_df_dict(
        mors_dict_parsed_floats, partial_replace_negatives
    )

    return mors_dict_removed_negatives
