from day_of_week import int_days_to_str


def test_day_sunday():
    assert int_days_to_str(1) == "Sunday"

def test_day_monday():
    assert int_days_to_str(2) == "Monday"

def test_day_tuesday():
    assert int_days_to_str(3) == "Tuesday"

def test_day_wednesday():
    assert int_days_to_str(4) == "Wednesday"

def test_day_thursday():
    assert int_days_to_str(5) == "Thursday"

def test_day_friday():
    assert int_days_to_str(6) == "Friday"

def test_day_saturday():
    assert int_days_to_str(7) == "Saturday"

def test_day_invalid_low():
    assert int_days_to_str(0) == "Invalid day"

def test_day_invalid_high():
    assert int_days_to_str(8) == "Invalid day"

def test_day_invalid_negative():
    assert int_days_to_str(-1) == "Invalid day"

def test_day_invalid_non_integer():
    assert int_days_to_str("three") == "Invalid input"