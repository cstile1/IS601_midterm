# app/calculator.py
from typing import Optional
from app.history import History
from app.calculator_config import CalculatorConfig

class Calculator:
    """
    Minimal skeleton:
    - holds a CalculatorConfig
    - owns a History instance
    (I'll add calculate/undo/redo next)
    """
    def __init__(self, config: Optional[CalculatorConfig] = None) -> None:
        self.config = config or CalculatorConfig()
        self.history = History()
