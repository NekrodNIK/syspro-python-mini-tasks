from src.task11 import cycle, chain


def test_cycle():
    saved = []
    i = 0
    for element in cycle((1, 2, 3)):
        saved.append(element)
        i += 1
        if i == 30:
            break

    assert saved == [1, 2, 3] * 10
            
        
def test_chain():
    saved = []
    for element in chain((1, 2, 3), [4, 5, 6], "789"):
        saved.append(element)

    assert saved == [1, 2, 3, 4, 5, 6, "7", "8", "9"]
