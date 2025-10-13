# app/calculator_config.py
from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class CalculatorConfig:
    """
    Minimal configuration for validations/calculations.
    Later, we’ll load these from .env (Day 6/7).
    """
    max_input_value: Decimal = Decimal("1000000000")  # 1e9 default
    precision: int = 4  # placeholder for rounding elsewhere
