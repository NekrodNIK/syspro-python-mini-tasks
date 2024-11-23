from src.task12 import coroutine

def test():
    @coroutine
    def func(i):
        while True:
            j = yield
            assert j == i

    for i in range(100):
        it = func(i)
        it.send(i)
