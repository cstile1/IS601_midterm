"""
tests/test_input_validators.py

Unit tests for the InputValidator class and its helper methods.
"""

import pytest
from decimal import Decimal
from app.input_validators import InputValidator
from app.calculator_config import CalculatorConfig
from app.exceptions import ValidationError


def test_validate_number_accepts_basic_values():
    cfg = CalculatorConfig(max_input_value=Decimal("100"))
    assert InputValidator.validate_number(5, cfg) == Decimal("5")
    assert InputValidator.validate_number("3.14", cfg) == Decimal("3.14")


def test_validate_number_rejects_invalid_input():
    cfg = CalculatorConfig(max_input_value=Decimal("10"))
    with pytest.raises(ValidationError):
        InputValidator.validate_number("abc", cfg)

def test_validate_number_rejects_overflow():
    cfg = CalculatorConfig(max_input_value=Decimal("10"))
    with pytest.raises(ValidationError):
        InputValidator.validate_number(Decimal("11"), cfg)  # exceeds max

def test_validate_number_trims_whitespace_and_signs():
    cfg = CalculatorConfig(max_input_value=Decimal("100"))
    assert InputValidator.validate_number("   -7.000  ", cfg) == Decimal("-7")

def test_validate_number_handles_large_but_valid_value():
    cfg = CalculatorConfig(max_input_value=Decimal("1000000"))
    assert InputValidator.validate_number("999999.9999", cfg) == Decimal("999999.9999")
