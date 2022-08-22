# import pytest
from fact import fact


def test_fact():
    assert fact(7) == 5040
    assert fact(5) == 120
    assert fact(0) == 1
    assert fact(-1) == -1
    assert fact(-2) == 2
    assert fact(-3) == -6
    assert fact(-4) == 24
