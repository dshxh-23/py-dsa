class DSAError(Exception):
    """Base class for all DSA exceptions"""
    pass


# ============== ARRAY EXCPETIONS ============ # 

class ArrayError(DSAError):
    """Base class for all array-related errors"""
    pass

class ArrayIndexOutOfBoundsError(ArrayError):
    """raised when invalid index is passed in as argument"""
    def __init__(self, message = "Array index out of bounds"):
        super().__init__(message)

class ArrayUnderflowError(ArrayError):
    """raised when an invalid operation is performed on an empty array"""
    def __init__(self, message = "Array is empty"):
        super().__init__(message)

class ArrayOverflowError(ArrayError):
    """raised when inserting element after it's already full"""
    def __init__(self, message = "Array is full. Cannot insert more elelments"):
        super().__init__(message)
        

# ============== LINKED LIST EXCEPTIONS ============ # 

class LinkedListError(DSAError):
    """Base class for linked list errors"""
    pass

class EmptyListError(LinkedListError):
    """Raised when operation is performed on empty list"""
    def __init__(self, message = "linked list is empty."):
        super().__init__(message)

class NodeNotFoundError(LinkedListError):
    """Raised when a node is not found in a linked list"""
    def __init__(self, message = "node not found in the list."):
        super().__init__(message)

class InvalidIndexError(LinkedListError):
    """raised when index (position) is invalid"""
    def __init__(self, message = "index is invalid."):
        super().__init__(message)


# ============== STACK EXCEPTIONS ============ # 

class StackError(DSAError):
    """Base class for all stack-related errors"""
    pass

class StackUnderflowError(StackError):
    """raised when an invalid operation is performed on an empty stack"""
    def __init__(self, message = "stack underflow."):
        super().__init__(message)

# Not required right now.
# class StackOverflowError(StackError):
#     """used for array_stack when size is fixed"""
#     def __init__(self, message = "stack overflow."):
#         super().__init__(message)


# ============== QUEUE EXCEPTIONS ============ # 

class QueueError(DSAError):
    """base class for all queue-related errors"""
    pass

class EmptyQueueError(QueueError):
    """raised when invalid operation is performed on an empty queue"""
    def __init__(self, message = "queue is empty."):
        super().__init__(message)


# ============== TREE EXCEPTIONS ============ # 

class TreeError(DSAError):
    """base class for all tree-related errors"""
    pass

class EmptyTreeError(TreeError):
    """raised when invalid operation is performed on an empty tree"""
    def __init__(self, message="tree is empty."):
        super().__init__(message)

class KeyNotFoundError(TreeError):
    """raised when a key does not exist in a tree"""
    def __init__(self, message = "key does not exist"):
        super().__init__(message)


class BSTError(TreeError):
    """base class for all BST-related errors"""
    pass

class DuplicateKeyError(BSTError):
    """raised when inserting a duplicate key in BST"""
    def __init__(self, message="cannot insert duplicate key."):
        super().__init__(message)