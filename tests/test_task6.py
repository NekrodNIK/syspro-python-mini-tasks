from src.task6 import flatten

def test_example1():
    result = flatten([1, 2, [4, 5], [6, [7]], 8])
    expected = [1, 2, 4, 5, 6, 7, 8]
    
    assert result == expected

def test_example2():
    result = flatten([1, 2, [4, 5], [6, [7]], 8], depth=1)
    expected = [1, 2, 4, 5, 6, [7], 8]
    
    assert result == expected
