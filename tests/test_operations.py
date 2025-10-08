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

def test_root_invalid():
    # b = 0 is invalid, should raise ValueError
    with pytest.raises(ValueError):
        operations.Root.execute(9, 0)

def test_modulus_basic():
    assert operations.Modulus.execute(10, 3) == 1

def test_modulus_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        operations.Modulus.execute(5, 0)

def test_int_divide_basic():
    assert operations.IntDivide.execute(7, 2) == 3

def test_int_divide_negative_flooring():
    # Python's // operator floors toward -infinity
    assert operations.IntDivide.execute(-7, 2) == -4

def test_int_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        operations.IntDivide.execute(7, 0)

def test_percent_basic():
    # 50 is 25% of 200
    assert operations.Percent.execute(50, 200) == 25

def test_percent_whole():
    # 200 is 100% of 200
    assert operations.Percent.execute(200, 200) == 100

def test_percent_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        operations.Percent.execute(5, 0)
