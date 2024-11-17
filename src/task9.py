import heapq


class LRUCache:
    def __init__(self, capacity=16):
        self.__capacity = capacity
        self.__cache = []

    def put(self, key, value):
        args = self.__cache, [0, key, value]

        if len(self.__cache) >= self.__capacity:
            heapq.heapreplace(*args)
        else:
            heapq.heappush(*args)

    def get(self, key):
        for i in range(len(self.__cache)):
            _, k, v = self.__cache[i]
            if k != key:
                continue

            self.__cache[i][0] += 1
            heapq.heapify(self.__cache)

            return v

        return None
