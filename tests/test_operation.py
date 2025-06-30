from src.maths_operations import add_numbers, subtract_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_subtract_numbers():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(0, 0) == 0
    assert subtract_numbers(-1, -1) == 0
    assert subtract_numbers(10, 5) == 5