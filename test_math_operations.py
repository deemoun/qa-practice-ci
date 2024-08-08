# test_math_operations.py

from math_operations import multiply, add

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 3) == 0

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 5) == 4
    assert add(0, 3) == 3
