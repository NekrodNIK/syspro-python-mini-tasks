from pytest import CaptureFixture

from src.task8 import format_table

expected = """\
| Benchmark | quick sort | merge sort | bubble sort |
|---------------------------------------------------|
| best      | 1.23       | 1.56       | 2.0         |
| worst     | 3.3        | 2.9        | 3.9         |
"""


def test(capsys: CaptureFixture):
    format_table(
        ["best", "worst"],
        ["quick sort", "merge sort", "bubble sort"],
        [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]],
    )

    assert capsys.readouterr()[0] == expected
