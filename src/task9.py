from heapq import heapify, heappush, heapreplace
from collections.abc import Hashable
from dataclasses import dataclass
from typing import Any


class LRUCache:
    @dataclass(order=True)
    class Element:
        priority: int
        key: Hashable
        value: Any

    def __init__(self, capacity=16):
        self.__capacity = capacity
        self.__filling = 0

        self.__heap: list[LRUCache.Element] = []
        self.__dict: dict[Hashable, LRUCache.Element] = {}

    def put(self, key: Hashable, value):
        el = LRUCache.Element(0, key, value)

        if self.__filling < self.__capacity:
            heappush(self.__heap, el)
            self.__filling += 1
        else:
            popped_el = heapreplace(self.__heap, el)
            self.__dict.pop(popped_el.key)

        self.__dict[key] = el

    def get(self, key: Hashable):
        el = self.__dict.get(key, None)
        if el is None:
            return None

        el.priority += 1
        heapify(self.__heap)
        return el.value

    @property
    def capacity(self):
        return self.__capacity

    @property
    def filling(self):
        return self.__filling
