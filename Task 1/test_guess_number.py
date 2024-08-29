from guess_number import check_guess


def test_guess_correct():
    assert check_guess(50, 50) == "Bingo"

def test_guess_high_guess():
    assert check_guess(50, 100) == "guess lower"

def test_guess_lower_guess():
    assert check_guess(100, 50) == "guess higher"

def test_guess_string_guess():
    assert check_guess(100, "twenty-four") == "Invalid input"

def test_out_of_range_guess():
    assert check_guess(100, 101) == "number out of range"
