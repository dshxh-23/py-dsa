class StaticArray:
    def __init__(self, cap):
        self._capacity = cap
        self._data = [None] * cap
        self._size = 0

    def insert(self, index, val):
        ...

    def append(self, val):
        ...

    def delete(self, index):
        ...

    def get(self, index):
        ...

    def set(self, index):
        ...

    def size(self):
        ...

    def capacity(self):
        ...

    def is_full(self):
        ...