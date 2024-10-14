from typing import Sequence


def my_zip(a: Sequence, b: Sequence) -> list[tuple]:
    return [(a[i], b[i]) for i in range(min(len(a), len(b)))]
