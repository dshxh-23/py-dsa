from core.nodes import Node

class LinkedStack:
    def ___init___(self):
        self.top = None
        self._size = 0
    
    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass

    def __bool__(self):
        return self.top is not None

    def __iter__(self):
        pass


    ###################


    def is_empty(self):
        return self.top is None

    
    def push(self, val):
        new = Node(val)
        new.next = self.top
        self.top = new
        self._size += 1


    def _empty(self):
        if self._size != 1:
            raise ...
        del_val = self.top.data        
        self.top = None
        self._size = 0
        return del_val
        
    def pop(self):
        if self.top is None:
            raise ...
        
        if self._size == 1:
            return self._empty()
        
        pop_val = self.top.data
        self.top = self.top.next
        return pop_val
        
    
    def peek(self):
        if self.top is None:
            raise ...
        return self.top.data

    
    def size(self):
        return self._size