from app.calculator import Calculator

calc = Calculator()


def test_add():
    assert calc.add(2, 3) == 5


def test_subtract():
    assert calc.subtract(5, 2) == 3


def test_multiply():
    assert calc.multiply(2, 4) == 8


def test_divide():
    assert calc.divide(10, 2) == 5
