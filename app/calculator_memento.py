#app/calculator_memento.py
from typing import List
from copy import deepcopy
from app.calculation import Calculation

class CalculatorMemento:
    """Immutable snapshot of the calculation history."""

    def __init__(self, state: List[Calculation]):
        # Deep copy ensures the snapshot is frozen at this moment in time
        self._state = deepcopy(state)

    def get_state(self) -> List[Calculation]:
        # Return a deep copy so the caller can’t mutate the snapshot
        return deepcopy(self._state)
