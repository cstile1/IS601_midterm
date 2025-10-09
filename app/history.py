#app/history.py
from typing import List
from copy import deepcopy
from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento

class History:
    """The History class keeps track of all past calculations and allows undo/redo.

    - _items is the current list of Calculation objects.
    - Each time we add or clear, we save a "snapshot" (CalculatorMemento) of the
      current state so we can go back if needed.
    - Undo restores the most recent snapshot from the undo stack.
    - Redo restores a snapshot that was undone."""
    def __init__(self) -> None:
        self._items: List[Calculation] = []
        self._undo_stack: List[CalculatorMemento] = []
        self._redo_stack: List[CalculatorMemento] = []

    # ----- Snapshot helpers -----
    def create_memento(self) -> CalculatorMemento:
        return CalculatorMemento(self._items)

    def restore(self, memento: CalculatorMemento) -> None:
        self._items = memento.get_state()

    # ----- Queries -----
    def items(self) -> List[Calculation]:
        return deepcopy(self._items)

    def size(self) -> int:
        return len(self._items)

    # ----- Mutations -----
    def add(self, calc: Calculation) -> None:
        self._undo_stack.append(self.create_memento())
        self._items.append(calc)
        self._redo_stack.clear()

    def clear(self) -> None:
        self._undo_stack.append(self.create_memento())
        self._items.clear()
        self._redo_stack.clear()

    # ----- Undo/Redo -----
    def can_undo(self) -> bool:
        return len(self._undo_stack) > 0

    def can_redo(self) -> bool:
        return len(self._redo_stack) > 0

    def undo(self) -> bool:
        if not self.can_undo():
            return False
        self._redo_stack.append(self.create_memento())
        prev = self._undo_stack.pop()
        self.restore(prev)
        return True

    def redo(self) -> bool:
        if not self.can_redo():
            return False
        self._undo_stack.append(self.create_memento())
        nxt = self._redo_stack.pop()
        self.restore(nxt)
        return True
