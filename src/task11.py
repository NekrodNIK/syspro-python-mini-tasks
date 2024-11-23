from collections.abc import Iterable
    
def cycle(iterable: Iterable) -> Iterable:
    saved = []
    for element in iterable:
        yield element
        saved.append(element)

    while saved:
        yield from saved

def chain(*args: Iterable) -> Iterable:
    for iterable in args:
        yield from iterable
                
