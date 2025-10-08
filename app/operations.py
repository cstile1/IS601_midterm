# app/operations.py

class Add:
    """Add two numbers."""
    @staticmethod
    def execute(a, b):
        return a + b


class Subtract:
    """Subtract b from a."""
    @staticmethod
    def execute(a, b):
        return a - b


class Multiply:
    """Multiply two numbers."""
    @staticmethod
    def execute(a, b):
        return a * b


class Divide:
    """Divide a by b. Raises ZeroDivisionError when b == 0."""
    @staticmethod
    def execute(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


class Power:
    """Raise a to the power b."""
    @staticmethod
    def execute(a, b):
        return a ** b


class Root:
    """
    Compute the b-th root of a (i.e., a ** (1/b)).
    Raises ValueError when b == 0.
    """
    @staticmethod
    def execute(a, b):
        if b == 0:
            raise ValueError("Cannot take zeroth root")
        return a ** (1 / b)
    
class Modulus:
    """Return a % b. Raises ZeroDivisionError when b == 0."""
    @staticmethod
    def execute(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot modulus by zero")
        return a % b

class IntDivide:
    """Return integer division a // b. Raises ZeroDivisionError when b == 0."""
    @staticmethod
    def execute(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot int_divide by zero")
        return a // b

class Percent:
    """Return (a / b) * 100. Raises ZeroDivisionError when b == 0."""
    @staticmethod
    def execute(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot compute percentage with denominator zero")
        return (a / b) * 100

class AbsDiff:
    """Return absolute difference |a - b|."""
    @staticmethod
    def execute(a, b):
        return abs(a - b)

