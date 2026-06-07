from core.exceptions import (
    ArrayOverflowError, 
    ArrayUnderflowError, 
    ArrayIndexOutOfBoundsError
)
from core.decorators.complexity import complexity, complexity_report

# ======================================== #

class StaticArray:
    def __init__(self, cap):
        self._capacity = cap
        self._data = [None] * cap
        self._size = 0


    # ---------- BASIC ----------

    @complexity(time='O(1)', space='O(1)')
    def size(self):
        return self._size

    @complexity(time='O(1)', space='O(1)')
    def capacity(self):
        return self._capacity

    @complexity(time='O(1)', space='O(1)')
    def is_full(self):
        return self._size == self._capacity
    
    @complexity(time='O(1)', space='O(1)')
    def is_empty(self):
        return self._size == 0


    # ---------- ACCESS ----------

    @complexity(time='O(1)', space='O(1)')
    def get(self, index):
        if index < 0 or index >= self._size:
            raise ArrayIndexOutOfBoundsError()
        return self._data[index]


    @complexity(time='O(1)', space='O(1)')
    def set(self, index, val):
        if index < 0 or index >= self._size:
            raise ArrayIndexOutOfBoundsError()
        self._data[index] = val
        

    # ---------- OPERATIONS ----------

    @complexity(time="O(n)", space="O(1)")
    def insert(self, index, val):
        if index < 0 or index > self._size:
            raise ArrayIndexOutOfBoundsError()
        
        if self.is_full():
            raise ArrayOverflowError()
        
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i-1]
        
        self._data[index] = val
        self._size += 1


    @complexity(time='O(1)', space='O(1)')
    def append(self, val):
        if self.is_full():
            raise ArrayOverflowError()
        
        self._data[self._size] = val
        self._size += 1


    @complexity(time='O(n)', space='O(1)')
    def delete(self, index):
        if self.is_empty():
            raise ArrayUnderflowError()
        
        if index < 0 or index >= self._size:
            raise ArrayIndexOutOfBoundsError()

        for i in range(index, self._size-1):
            self._data[i] = self._data[i+1]
        self._data[self._size-1] = None

        self._size -= 1


    # ---------- DUNDER METHODS ----------

    def __bool__(self):
        return not self.is_empty()

    # ----------

    def __len__(self):
        return self.size()
    
    # ----------

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise ArrayIndexOutOfBoundsError()
        return self._data[index]

    # ----------

    def __setitem__(self, index, val):
        if index < 0 or index >= self._size:
            raise ArrayIndexOutOfBoundsError()
        self._data[index] = val

    # ----------

    def __iter__(self):
        for i in range(self._size):
            yield self._data[i]

    # ----------

    def __repr__(self):
        return f"StaticArray({list(self)})"

    # ----------

    def __str__(self):
        return f"[{', '.join(str(self._data[i]) for i in range(self._size))}]"


# ======================================== #


def main():
    arr = StaticArray(10)
    arr.append(1)
    arr.append(1)
    arr.append(3)
    arr.append(5)
    print(arr)
    arr.insert(2, 2)
    print(arr)
    arr.delete(1)
    print(arr)



if __name__ == "__main__":
    main()