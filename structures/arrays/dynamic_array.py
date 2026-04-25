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
        pass

    # ----------

    def capacity(self):
        pass

    # ----------

    def is_empty(self):
        pass

    
    # ---------- ACCESS ----------
    
    def get():
        pass

    # ----------

    def set():
        pass

    
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



    