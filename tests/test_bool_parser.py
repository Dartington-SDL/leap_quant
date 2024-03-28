from ..helper_functions import parse_binary_to_boolean
def test_parse_binary_to_boolean():
   
    true_binary = 1
    bool = parse_binary_to_boolean(true_binary)

    assert True == bool




    