import pytest
from calculator import Calculator

calc = Calculator()


def test_add_positive_numbers():
    assert calc.add(5, 3) == 8


def test_add_zero():
    assert calc.add(10, 0) == 10


def test_add_negative_numbers():
    assert calc.add(-5, 3) == -2


def test_subtract_positive_numbers():
    assert calc.subtract(5, 3) == 2


def test_subtract_result_is_negative():
    assert calc.subtract(10, 20) == -10


def test_subtract_negative_numbers():
    assert calc.subtract(-5, -3) == -2


def test_multiply_positive_numbers():
    assert calc.multiply(5, 3) == 15


def test_multiply_by_zero():
    assert calc.multiply(10, 0) == 0


def test_multiply_negative_numbers():
    assert calc.multiply(-5, 3) == -15


def test_divide_positive_numbers():
    assert calc.divide(10, 2) == 5


def test_divide_negative_number():
    assert calc.divide(-10, 2) == -5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(10, 0)
