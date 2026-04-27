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
    
    def append(self, val):
        """insert element at end of array"""

        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        
        self._data[self._size] = val
        self._size += 1

    # ----------

    def insert(self, index, val):
        """insert an element at a particular index"""

        if index < 0 or index > self._size:
            raise ArrayIndexOutOfBoundsError()
        
        # resize dynamic array if capacity full
        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        # shift right
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i-1]

        self._data[index] = val
        self._size += 1 

    # ----------

    def delete(self, index):
        """deletes a element at a specific index"""

        if self.is_empty():
            raise ArrayUnderflowError()       

        if index < 0 or index >= self._size:
            raise ArrayIndexOutOfBoundsError()
        
        value = self._data[index]
        
        for i in range(index, self._size):
            self._data[i] = self._data[i+1]
        
        self._size -= 1
        return value


    # ---------- INTERNAL ----------

    def _resize(self, new_cap):
        new_data = [None] * new_cap
        for i in range(self._size):
            new_data[i] = self._data[i]

        self._data = new_data
        self._capacity = new_cap

    # ---------- DUNDER METHODS ----------

    def __bool__(self):
        return not self.is_empty()

    # ----------

    def __len__(self):
        return self._size

    # ----------

    def __iter__(self):
        for i in range(self._size):
            yield self._data[i]

    # ----------

    def __repr__(self):
        return f"DynamicArray({list(self)})"

    # ----------
    
    def __str__(self):
        if self.is_empty():
            return "Array is Empty"
        return f"[{', '.join(str(self._data[i]) for i in range(self._size))}]"
    

# ======================================== #


def main():
    arr = DynamicArray()
    print(arr)
    arr.append(10)
    print(arr)
    arr.append(20)
    arr.append(30)
    print(arr)
    arr.delete(1)
    arr.insert(1, 100)
    print(arr)
    print("array size: ", arr.size())



if __name__ == "__main__":
    main()