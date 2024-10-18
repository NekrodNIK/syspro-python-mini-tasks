from src.task5 import specialize


def sum_(x, y):
    return x + y


def test_opt_decorator():
    assert specialize(sum_, 1, 4)() == 5


def test_key_decorator():
    assert specialize(sum_, x=1, y=4)() == 5


def test_opt_func():
    assert specialize(sum_)(1, 4) == 5


def test_key_func():
    assert specialize(sum_)(x=1, y=4) == 5


def test_mixed():
    assert specialize(sum_, y=1)(4) == 5
