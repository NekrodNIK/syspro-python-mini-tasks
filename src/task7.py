from collections.abc import Callable
import functools


def deprecated(func=None, *, since=None, will_be_removed=None) -> Callable:
    if func is None:
        return functools.partial(
            deprecated, since=since, will_be_removed=will_be_removed
        )

    out = "".join(
        (
            f"Warning: function {func.__name__} is deprecated",
            f" since version {since}" if since else "",
            ". ",
            "It will be removed in ",
            f"version {will_be_removed}" if will_be_removed else "future versions",
            ".",
        )
    )

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(out)

        return func(*args, **kwargs)

    return wrapper
