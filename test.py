# test_calculator.py
import pytest
from calculator import add, sub, multi, div

def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_sub():
    assert sub(10, 5) == 5
    assert sub(0, 5) == -5
    assert sub(5, 10) == -5

def test_multi():
    assert multi(3, 5) == 15
    assert multi(-3, 5) == -15
    assert multi(0, 5) == 0

def test_div():
    assert div(10, 2) == 5
    assert div(9, 3) == 3
    assert div(-6, 2) == -3

    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        div(5, 0)

