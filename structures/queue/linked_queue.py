from core.nodes import Node
from core.exceptions import EmptyQueueError

class LinkedQueue():
    def __init__(self):
        self.front = None   # Head of linked list
        self.rear = None    # Tail of linked list
        self._size = 0
        

    def __repr__(self):
        pass

    def __len__(self):
        return self._size

    def __iter__(self):
        curr = self.front
        while curr:
            yield curr.data
            curr = curr.next

    def __bool__(self):
        return self.front is None and self.rear is None

    def __str__(self):
        if self._size == 0:
            return f"queue is empty"
        queue = [str(element) for element in self]
        return f"(f) {' - '.join(queue)} (r)"
    


    def enqueue(self, val):
        """insert at rear"""
        new = Node(val)

        if self.rear is None and self.front is None:
            self.front = new
            self.rear = new
            self._size += 1
            return

        self.rear.next = new
        self.rear = new
        self._size += 1


    def _empty(self):
        """internal helper to cleanly delete last value"""
        if self._size != 1:
            return
        
        del_val = self.front.data
        
        self.front = None
        self.rear = None
        self._size = 0
        return del_val


    def dequeue(self):
        """delete at front"""
        if self.rear is None and self.front is None:
            raise EmptyQueueError
        
        if self._size == 1:
            return self._empty()

        del_val = self.front.data
        self.front = self.front.next
        self._size -= 1
        return del_val
                


    def peek(self):
        """return front of the queue"""
        if self.front is None and self.rear is None:
            raise EmptyQueueError
        return self.top.data

    def is_empty(self):
        """check weather the queue is empty or not"""
        return self.front is None and self.rear is None

    def size(self):
        """return the size of the queue"""
        return self._size



def main():
    q = LinkedQueue()
    print(q)
    q.enqueue(10)
    q.enqueue(20)
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())


if __name__ == "__main__":
    main()