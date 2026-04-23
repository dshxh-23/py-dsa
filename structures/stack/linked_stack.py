from core.nodes import Node
from core.exceptions import StackUnderflowError

class LinkedStack:
    def __init__(self):
        self.top = None
        self._size = 0
    
    def __repr__(self):
        pass

    def __str__(self):
        stack = [str(element) for element in self]
        return " | ".join(stack)

    def __len__(self):
        return self._size

    def __bool__(self):
        return self.top is not None

    def __iter__(self):
        curr = self.top
        while curr:
            yield curr.data
            curr = curr.next


    ###################


    def is_empty(self):
        """check if stack is empty or not"""
        return self.top is None

    
    def push(self, val):
        """add element to top of the stack"""
        new = Node(val)
        new.next = self.top
        self.top = new
        self._size += 1


    def _empty(self):
        """internal helper to cleanly empty the stack and return the it's top"""
        del_val = self.top.data        
        self.top = None
        self._size = 0
        return del_val
        
    def pop(self):
        """pop the top element of the stack"""
        if self.top is None:
            raise StackUnderflowError
        
        if self._size == 1:
            return self._empty()
        
        pop_val = self.top.data
        self.top = self.top.next
        self._size -= 1
        return pop_val
        
    
    def peek(self):
        """return the top of the stack"""
        if self.top is None:
            raise StackUnderflowError()
        return self.top.data

    
    def size(self):
        """return the size of the stack"""
        return self._size
    

def main():
    ls1 = LinkedStack()
    ls1.push(10)
    ls1.push(20)

    print(ls1)          # 20 | 10
    print(ls1.pop())    # 20
    print(ls1)          # 10
    print(ls1.pop())    # 10

    # print(ls1.pop())
    # print(ls1.peek())

    ls1.push(30)
    print(ls1.peek())
    ls1.push(40)
    print(ls1.peek())

if __name__ == "__main__":
    main()