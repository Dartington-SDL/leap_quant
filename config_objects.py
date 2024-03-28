from typing import Dict

# MORS columns datatype map
pandas_dtype_map: Dict[str, str] = {  # Directly using str annotations since these are interpreted by pandas
    "OBJECT": "object",
    "INT": "int64",
    "FLOAT": "float64",
    "BOOL": "bool",
    "DATETIME": "datetime64[ns]",
    "TIMEDELTA": "timedelta64[ns]",
    "CATEGORY": "category"
}

# Dictionary of column name and datatype for each DF
column_datatype_dict = {
    'leap_user_key': pandas_dtype_map['INT'],
    # Convert to date object
    'assessment_date': pandas_dtype_map['DATETIME'],
    'assessment_tool': pandas_dtype_map['CATEGORY'],
    'event': pandas_dtype_map['CATEGORY'],
    'age_at_registration': pandas_dtype_map['INT'],
    'ethnicity_b': pandas_dtype_map['CATEGORY'],
    'home_language': pandas_dtype_map['CATEGORY'],
    'lone_parent': pandas_dtype_map['CATEGORY'],
    'lsoacode': pandas_dtype_map['CATEGORY'],
    'ward_name': pandas_dtype_map['CATEGORY'],
    'ward_code': pandas_dtype_map['CATEGORY'],
    'borough': pandas_dtype_map['CATEGORY'],
    'lsoaname': pandas_dtype_map['CATEGORY'],
    'imdscore': pandas_dtype_map['FLOAT'],
    'imddecile': pandas_dtype_map['FLOAT'],
    'f1': pandas_dtype_map['FLOAT'],
    'decile_1': pandas_dtype_map['FLOAT'],
    'imd_local_dec': pandas_dtype_map['FLOAT'],
    'imd_local_quint': pandas_dtype_map['FLOAT'],
    'mergestatus': pandas_dtype_map['CATEGORY'],
    'bab_total_dosage': pandas_dtype_map['INT'],
    # Change 0 and 1 to True/False 
    'bab_reached_dosage_yn': pandas_dtype_map['BOOL'], 
    # Convert to date object
    'bab_date_reached_dosage': pandas_dtype_map['DATETIME'],
    'ptt_total_dosage': pandas_dtype_map['INT'],
     # Change 0 and 1 to True/False 
    'ptt_reached_dosage_yn': pandas_dtype_map['BOOL'], 
    # Convert to date object
    'ptt_date_reached_dosage': pandas_dtype_map['DATETIME'],
    'cos_total_dosage': pandas_dtype_map['INT'],
     # Change 0 and 1 to True/False 
    'cos_reached_dosage_yn': pandas_dtype_map['BOOL'], 
    # Convert to date object
    'cos_date_reached_dosage': pandas_dtype_map['DATETIME'],
    'warmth_total': pandas_dtype_map['INT'],
    'invasion_total': pandas_dtype_map['INT'],
    'invasion_final': pandas_dtype_map['INT'],
    'warmth_final': pandas_dtype_map['INT'],
    'total_final': pandas_dtype_map['INT'],
}
