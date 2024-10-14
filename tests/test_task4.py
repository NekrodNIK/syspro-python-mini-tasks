from src.task4 import reverse_dict
import pytest


def test_example():
    request = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}
    expected = {97832: ("Ivanov", "Kuznecov"), 55521: "Petrov"}

    assert reverse_dict(request) == expected


def test_general():
    request = {n: n % 2 for n in range(1000)}
    expected = {
        1: tuple(n for n in range(1000) if n % 2 == 1),
        0: tuple(n for n in range(1000) if n % 2 == 0),
    }

    assert reverse_dict(request) == expected


def test_raise_error():
    with pytest.raises(TypeError):
        reverse_dict({1: []})
