from src.task7 import deprecated
from pytest import CaptureFixture


sum_1 = deprecated(sum)
sum_2 = deprecated(since="1.0.0")(sum)
sum_3 = deprecated(will_be_removed="2.0.0")(sum)
sum_4 = deprecated(since="1.0.0", will_be_removed="2.0.0")(sum)

expected_1 = (
    f"Warning: function {sum.__name__} is deprecated. "
    "It will be removed in future versions.\n"
)

expected_2 = (
    f"Warning: function {sum.__name__} is deprecated since version 1.0.0. "
    "It will be removed in future versions.\n"
)

expected_3 = (
    f"Warning: function {sum.__name__} is deprecated. "
    "It will be removed in version 2.0.0.\n"
)

expected_4 = (
    f"Warning: function {sum.__name__} is deprecated since version 1.0.0. "
    "It will be removed in version 2.0.0.\n"
)


def test(capsys: CaptureFixture):
    sum_1((1,))
    assert capsys.readouterr()[0] == expected_1

    sum_2((1,))
    assert capsys.readouterr()[0] == expected_2

    sum_3((1,))
    assert capsys.readouterr()[0] == expected_3

    sum_4((1,))
    assert capsys.readouterr()[0] == expected_4
