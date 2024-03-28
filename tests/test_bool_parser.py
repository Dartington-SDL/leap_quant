from ..helper_functions import parse_binary_to_boolean

def test_parse_binary_to_boolean_true_cases():
    # Test with a float input
    float_true = 1.0
    bool_from_float = parse_binary_to_boolean(float_true)
    assert True is bool_from_float, "Failed on float input"
    
    # Test with a string input
    string_true = "1.0"
    bool_from_string = parse_binary_to_boolean(string_true)
    assert True is bool_from_string, "Failed on string input"
    
    # Test with an integer input
    int_true = 1
    bool_from_int = parse_binary_to_boolean(int_true)
    assert True is bool_from_int, "Failed on integer input"


def test_parse_binary_to_boolean_negative():
    # Test with a float input
    float_false = 0.0
    bool_from_float = parse_binary_to_boolean(float_false)
    assert False is bool_from_float, "Failed on float input (expected False)"
    
    # Test with a string input
    string_false = "0.0"
    bool_from_string = parse_binary_to_boolean(string_false)
    assert False is bool_from_string, "Failed on string input (expected False)"
    
    # Test with an integer input
    int_false = 0
    bool_from_int = parse_binary_to_boolean(int_false)
    assert False is bool_from_int, "Failed on integer input (expected False)"