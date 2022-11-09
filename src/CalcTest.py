from .Calc import Calc


def test_addition_int():
    calc = Calc()
    result = calc.addition_int(5, 5)
    assert result == 10


def test_addtion_array():
    calc = Calc()
    result = calc.addition_int_array([5, 5, 5])
    assert result == 15


def test_validate_result():
    calc = Calc()
    result = calc.validate_result(5, 5)
    assert result == True

    result = calc.validate_result(4, 5)
    assert result == False
