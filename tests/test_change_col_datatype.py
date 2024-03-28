import pandas as pd
from ..helper_functions import map_dataframe_dtypes

def test_change_col_datatype():
    raw_df = pd.DataFrame({
        "name": ["Tom", "Dick", "Harry"],
        "age": [22, 37, 66],
        "is_parent": [True, False, True],
        "actual_bool": [True, False, True]
    })

    assert raw_df["age"].dtype == "int64"
    assert raw_df["is_parent"].dtype == "bool"
    assert raw_df["actual_bool"].dtype == "bool"

    dtype_map = {
        "name": "object",
        "age": "int32" ,
        "is_parent": "bool",
        "actual_bool": "bool"
    }
    
    mapped_dtype_df: pd.DataFrame = map_dataframe_dtypes(raw_df, dtype_map)

    assert mapped_dtype_df["name"].dtype == "object"
    assert mapped_dtype_df["age"].dtype == "int"

