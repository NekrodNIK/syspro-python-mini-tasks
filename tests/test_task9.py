from src.task9 import LRUCache


def test():
    cache = LRUCache(capacity=3)
    
    cache.put('a', 1)
    cache.put('b', 2)
    cache.put('c', 3)

    assert cache.get('a') == 1
    assert cache.get('b') == 2
    assert cache.get('c') == 3

    cache.get('a')
    cache.get('b')
    cache.put('d', 4)

    assert cache.get('c') == None
    assert cache.get('d') == 4
    
