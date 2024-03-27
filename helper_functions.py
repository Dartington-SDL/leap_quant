def reduce_df_dict_by_pattern(df_dict, function, pattern):
    """
    Transforms each DataFrame in a dictionary by applying a specified function with a pattern.

    This function iterates over a dictionary of DataFrames, applying a given function to each
    DataFrame. The function is applied with an additional pattern argument, allowing for specific
    transformations based on the pattern (e.g., removing columns that match the pattern).

    Parameters:
        df_dict (dict): A dictionary where keys are identifiers and values are pandas DataFrames.
        function (callable): A function that takes a DataFrame and a pattern string as arguments
                             and returns a transformed DataFrame.
        pattern (str): A pattern string to be passed to the function for transforming each DataFrame.

    Returns:
        dict: A dictionary with the same keys as `df_dict` but with the values being the transformed
              DataFrames.
    """
    dict_keys = df_dict.keys()
    dict_values = df_dict.values()

    # Create empty list to put dataframes into
    transformed_values = []

    for value in dict_values:
        transformed_values.append(function(value, pattern))

    transformed_dict = dict(zip(dict_keys, transformed_values))

    return transformed_dict
