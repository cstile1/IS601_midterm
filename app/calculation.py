# app/calculation.py
from app import operations
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Calculation:
    """Represents one calculation with inputs, result, and timestamp."""
    operation: str
    a: float
    b: float
    result: float
    timestamp: datetime = datetime.utcnow()

class OperationFactory:
    """Factory that returns the correct operation class based on a string name"""

    OPS = {
        "add": operations.Add,
        "subtract": operations.Subtract,
        "multiply": operations.Multiply,
        "divide": operations.Divide,
        "power": operations.Power,
        "root": operations.Root,
        "modulus": operations.Modulus,
        "int_divide": operations.IntDivide,
        "percent": operations.Percent,
        "abs_diff": operations.AbsDiff,
    }

    @classmethod
    def get(cls, name: str):
        """
        Given a string like 'add' or 'divide', return the matching class
        Example: OperationFactory.get("add") -> Add
        """
        if name in cls.OPS:
            return cls.OPS[name]
        else:
            raise ValueError(f"Unknown operation: {name}")
