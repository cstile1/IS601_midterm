#tests/test_calculation.py
import pytest
from app.calculation import OperationFactory
from app import operations
from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento
from app.history import History

def test_factory_returns_correct_classes():
    """This tests whether the Factory is working correctly"""
    assert OperationFactory.get("add") is operations.Add
    assert OperationFactory.get("subtract") is operations.Subtract
    assert OperationFactory.get("multiply") is operations.Multiply
    assert OperationFactory.get("divide") is operations.Divide
    assert OperationFactory.get("power") is operations.Power
    assert OperationFactory.get("root") is operations.Root

def test_factory_unknown_operation():
    with pytest.raises(ValueError):
        OperationFactory.get("banana")

def test_factory_new_operations():
    """Test that new operations are correctly mapped in the Factory"""
    assert OperationFactory.get("modulus") is operations.Modulus
    assert OperationFactory.get("int_divide") is operations.IntDivide
    assert OperationFactory.get("percent") is operations.Percent
    assert OperationFactory.get("abs_diff") is operations.AbsDiff

def test_calculation_fields_are_stored_correctly():
    c = Calculation("add", 2, 3, 5)
    assert c.operation == "add"
    assert c.a == 2
    assert c.b == 3
    assert c.result == 5

def test_memento_restores_history_snapshot():
    from app.calculation import Calculation
    history_state = [Calculation("add", 1, 2, 3)]
    memento = CalculatorMemento(history_state)

    # modify original list after snapshot
    history_state.append(Calculation("multiply", 2, 3, 6))

    # memento should still have the original single item
    restored = memento.get_state()
    assert len(restored) == 1
    assert restored[0].result == 3

def test_history_add_and_undo_redo_roundtrip():
    from app.calculation import Calculation
    h = History()

    h.add(Calculation("add", 2, 3, 5))
    h.add(Calculation("multiply", 3, 4, 12))
    assert h.size() == 2

    # Undo should go back to 1
    assert h.undo() is True
    assert h.size() == 1

    # Redo should go forward again
    assert h.redo() is True
    assert h.size() == 2

def test_history_clear_and_undo():
    from app.calculation import Calculation
    h = History()
    h.add(Calculation("power", 2, 3, 8))
    h.add(Calculation("root", 9, 2, 3))
    assert h.size() == 2

    h.clear()
    assert h.size() == 0
    assert h.undo() is True
    assert h.size() == 2

def test_history_edge_cases():
    from app.calculation import Calculation
    h = History()
    # nothing to undo yet
    assert h.undo() is False
    # add one, undo once, second undo fails
    h.add(Calculation("add", 1, 1, 2))
    assert h.undo() is True
    assert h.undo() is False
    # redo once works, second redo fails
    assert h.redo() is True
    assert h.redo() is False