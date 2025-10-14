# tests/test_calculator.py
from decimal import Decimal
from app.calculator import Calculator
from app.calculator_config import CalculatorConfig
from app.exceptions import ValidationError
import pytest

def test_calculator_add_and_history():
    cfg = CalculatorConfig(precision=2, max_input_value=Decimal("1000000"))
    calc = Calculator(config=cfg)
    res = calc.calculate("add", 2, 3)
    assert res == 5.00

    items = calc.history.items()
    assert len(items) == 1
    assert items[0].operation == "add"
    assert items[0].result == 5.00

def test_calculator_multiply_minimal():
    calc = Calculator()
    assert calc.calculate("multiply", 2, 4) == 8

def test_calculator_divide_happy_and_zero_guard():
    calc = Calculator()
    # happy path: 10 / 4 = 2.5
    assert calc.calculate("divide", 10, 4) == 2.5
    # error path: divide by zero should raise ValidationError
    with pytest.raises(ValidationError):
        calc.calculate("divide", 5, 0)

def test_calculator_power():
    calc = Calculator()
    # 2^3 = 8
    assert calc.calculate("power", 2, 3) == 8

def test_calculator_root_and_zero_guard():
    calc = Calculator()
    # happy path: square root of 9 is 3
    assert calc.calculate("root", 9, 2) == 3
    # error path: zeroth root should raise
    with pytest.raises(ValidationError):
        calc.calculate("root", 9, 0)

def test_calculator_modulus_and_guard():
    calc = Calculator()
    # happy path
    assert calc.calculate("modulus", 10, 3) == 1
    # zero divisor should raise
    with pytest.raises(ValidationError):
        calc.calculate("modulus", 10, 0)

def test_calculator_int_divide_and_guard():
    calc = Calculator()
    # happy path (integer/floor division)
    assert calc.calculate("int_divide", 7, 2) == 3
    # zero divisor should raise
    with pytest.raises(ValidationError):
        calc.calculate("int_divide", 7, 0)

def test_calculator_percent_and_guard():
    calc = Calculator()
    # happy path: 50 is 25% of 200
    assert calc.calculate("percent", 50, 200) == 25
    # zero denominator should raise
    with pytest.raises(ValidationError):
        calc.calculate("percent", 5, 0)