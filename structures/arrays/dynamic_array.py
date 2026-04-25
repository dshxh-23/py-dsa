from core.exceptions import (
    ArrayIndexOutOfBoundsError,
    ArrayUnderflowError
)


# ======================================== #


class DynamicArray:
    def __init__(self, cap = 1):
        self._capacity = cap
        self._size = 0
        self._data = [None] * self._capacity


    # ---------- BASIC ----------

    def size(self):
        return self._size

    # ----------

    def capacity(self):
        return self._capacity

    # ----------

    def is_empty(self):
        return self._size == 0

    
    # ---------- ACCESS ----------
    
    def get(self, index):
        if index < 0 or index >= self._size:
            raise ArrayIndexOutOfBoundsError()
        return self._data[index]

    # ----------

    def set(self, index, val):
        if index < 0 or index >= self._size:
            raise ArrayIndexOutOfBoundsError()
        self._data[index] = val

    
    # ---------- OPERATIONS ----------
    
    def append():
        pass

    # ----------

    def insert():
        pass

    # ----------

    def delete():
        pass


    # ---------- HELPER ----------

    def _resize(self):
        pass

    # ---------- DUNDER METHODS ----------

    def __bool__(self):
        pass

    # ----------

    def __len__(self):
        pass

    # ----------

    def __iter__(self):
        pass

    # ----------

    def __repr__(self):
        pass

    # ----------
    
    def __str__(self):
        pass



    