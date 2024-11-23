from src.task12 import coroutine

def test():
    @coroutine
    def func():
        return iter([1, 2, 3, 4, 5])

    assert list(func()) == [2, 3, 4, 5]
