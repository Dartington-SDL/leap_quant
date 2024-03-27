from datetime import datetime
from helper_functions import parse_mors_datestring
def test_string_to_date():
    # arrange
    datestring = "01jun2019"
    datetime_object = datetime.strptime("2019-06-01")

    assert parse_mors_datestring(datestring) == datetime_object




    