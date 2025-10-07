# app/calculation.py
from app import operations

class OperationFactory:
    """Factory that returns the correct operation class based on a string name"""

    OPS = {
        "add": operations.Add,
        "subtract": operations.Subtract,
        "multiply": operations.Multiply,
        "divide": operations.Divide,
        "power": operations.Power,
        "root": operations.Root,
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
