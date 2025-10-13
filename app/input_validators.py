# app/input_validators.py
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from typing import Any
from app.calculator_config import CalculatorConfig
from app.exceptions import ValidationError

@dataclass
class InputValidator:
    """Validates and sanitizes calculator inputs using Decimal and config."""

    @staticmethod
    def validate_number(value: Any, config: CalculatorConfig) -> Decimal:
        """
        Convert input to Decimal, enforce max range, and normalize.
        Accepts ints/floats/strings like '3.14' (stripped).
        Raises ValidationError for invalid or out-of-range values.
        """
        try:
            if isinstance(value, str):
                value = value.strip()
            number = Decimal(str(value))  # robust conversion via string form
            if abs(number) > config.max_input_value:
                raise ValidationError(
                    f"Value exceeds maximum allowed: {config.max_input_value}"
                )
            # normalize to remove trailing zeros (e.g., Decimal('3.1400') -> Decimal('3.14'))
            return number.normalize()
        except InvalidOperation as e:
            raise ValidationError(f"Invalid number format: {value!r}") from e
