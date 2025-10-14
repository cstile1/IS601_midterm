# tests/test_calculator.py
from decimal import Decimal
from app.calculator import Calculator
from app.calculator_config import CalculatorConfig
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
