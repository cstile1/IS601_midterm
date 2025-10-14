# app/calculator.py
from typing import Optional
from decimal import Decimal

from app.calculation import Calculation, OperationFactory
from app.history import History
from app.input_validators import InputValidator
from app.exceptions import ValidationError
from app.calculator_config import CalculatorConfig


class Calculator:
    """
    Orchestrates a calculation:
      1) Validate inputs using InputValidator + CalculatorConfig (Decimal).
      2) Guard invalid cases (e.g., divisor/root = 0).
      3) Look up the operation via OperationFactory and execute.
      4) Round result to config.precision.
      5) Record the Calculation in History.

    Also exposes undo/redo/clear_history via the History instance.
    """

    def __init__(self, config: Optional[CalculatorConfig] = None) -> None:
        self.config = config or CalculatorConfig()
        self.history = History()

    def calculate(self, op_name: str, a, b) -> float:
        """
        Validate inputs, run the selected operation, round, and store in history.
        Returns the (rounded) float result.
        """
        # 1) Validate/coerce inputs (Decimal) and enforce max range
        da: Decimal = InputValidator.validate_number(a, self.config)
        db: Decimal = InputValidator.validate_number(b, self.config)

        # 2) Operation-specific guards before executing
        if op_name in ("divide", "int_divide", "modulus", "percent") and db == 0:
            raise ValidationError("Division/modulus/percent by zero is not allowed.")
        if op_name == "root" and db == 0:
            raise ValidationError("Cannot take zeroth root.")

        # 3) Execute via the factory (operations expect regular numbers)
        op_cls = OperationFactory.get(op_name)
        a_num = float(da)
        b_num = float(db)
        result = op_cls.execute(a_num, b_num)

        # 4) Round to configured precision (non-negative int)
        if isinstance(self.config.precision, int) and self.config.precision >= 0:
            result = round(result, self.config.precision)

        # 5) Record in history as an immutable Calculation
        self.history.add(
            Calculation(operation=op_name, a=a_num, b=b_num, result=result)
        )
        return result

    # ---- History convenience methods ----
    def undo(self) -> bool:
        return self.history.undo()

    def redo(self) -> bool:
        return self.history.redo()

    def clear_history(self) -> None:
        self.history.clear()
