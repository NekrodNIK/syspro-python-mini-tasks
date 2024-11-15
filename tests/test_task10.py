from src.task10 import SingletonMetaClass


def test():
    class Singleton1(metaclass=SingletonMetaClass): ...

    class Singleton2(metaclass=SingletonMetaClass): ...

    assert Singleton1() is Singleton1()
    assert Singleton2() is Singleton2()
    assert Singleton1() is not Singleton2()
