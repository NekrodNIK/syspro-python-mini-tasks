from src.task7 import deprecated
from pytest import CaptureFixture


@deprecated
def func1():
    pass


@deprecated(since="1.0.0")
def func2():
    pass


@deprecated(will_be_removed="2.0.0")
def func3():
    pass


@deprecated(since="1.0.0", will_be_removed="2.0.0")
def func4():
    pass


expected_1 = (
    f"Warning: function {func1.__name__} is deprecated. "
    "It will be removed in future versions.\n"
)

expected_2 = (
    f"Warning: function {func2.__name__} is deprecated since version 1.0.0. "
    "It will be removed in future versions.\n"
)

expected_3 = (
    f"Warning: function {func3.__name__} is deprecated. "
    "It will be removed in version 2.0.0.\n"
)

expected_4 = (
    f"Warning: function {func4.__name__} is deprecated since version 1.0.0. "
    "It will be removed in version 2.0.0.\n"
)


def test(capsys: CaptureFixture):
    func1()
    assert capsys.readouterr()[0] == expected_1

    func2()
    assert capsys.readouterr()[0] == expected_2

    func3()
    assert capsys.readouterr()[0] == expected_3

    func4()
    assert capsys.readouterr()[0] == expected_4
