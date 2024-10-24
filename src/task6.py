from collections.abc import Iterable


def flatten(obj: Iterable, depth=float("inf")) -> list:
    result = []

    for el in obj:
        if depth > 0 and isinstance(el, Iterable):
            result += flatten(el, depth - 1)
        else:
            result.append(el)

    return result

