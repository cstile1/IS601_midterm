# tests/test_operations.py
import pytest
from app import operations

def test_add():
    assert operations.Add.execute(2, 3) == 5

def test_subtract():
    assert operations.Subtract.execute(5, 2) == 3

def test_multiply():
    assert operations.Multiply.execute(3, 4) == 12

def test_divide():
    assert operations.Divide.execute(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        operations.Divide.execute(10, 0)

def test_power():
    assert operations.Power.execute(2, 3) == 8

def test_root_square():
    assert operations.Root.execute(9, 2) == 3