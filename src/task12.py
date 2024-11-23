from collections.abc import Callable, Iterator


def coroutine(func: Callable[..., Iterator]):
    def wrapper(*args, **kwargs):
        iterable = func(*args, **kwargs)
        next(iterable)
        return iterable

    return wrapper
