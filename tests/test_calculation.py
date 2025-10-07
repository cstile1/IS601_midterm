#tests/test_calculation.py
import pytest
from app.calculation import OperationFactory
from app import operations

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