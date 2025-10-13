# app/exceptions.py

class CalculatorError(Exception):
    """Base class for calculator-specific errors."""

class OperationError(CalculatorError):
    """Raised when an operation fails or is unsupported."""

class ValidationError(CalculatorError):
    """Raised when user inputs are invalid (type, range, etc.)."""

class PersistenceError(CalculatorError):
    """Raised when saving/loading history fails."""
# app/exceptions.py

class CalculatorError(Exception):
    """Base class for calculator-specific errors."""

class OperationError(CalculatorError):
    """Raised when an operation fails or is unsupported."""

class ValidationError(CalculatorError):
    """Raised when user inputs are invalid (type, range, etc.)."""

class PersistenceError(CalculatorError):
    """Raised when saving/loading history fails."""
