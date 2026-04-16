from core.nodes import TreeNode
from core.exceptions import *       # Replace * with specific errors used

from data_structures.queue.linked_queue import LinkedQueue

# ======================================== #

class BinarySearchTree():

    def __init__(self):
        self.root = None
        self._size = 0

    
    # ---------- DUNDER METHODS ----------

    def __repr__(self):
        pass

    def __bool__(self):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def __str__(self):
        pass

    # ---------- CORE UTILS ----------

    def is_empty(self):
        return True if self.root is None else False


    def size(self):
        return self._size


    # ---------- BASIC OPERAITONS ----------

    def insert(self, val):
        new_node = TreeNode(val)

        if self.root is None:
            self.root = new_node
            self._size += 1
            return self.root
        
        parent = None
        curr = self.root

        while curr:
            parent = curr
            if new_node.data < curr.data:
                curr = curr.left
            
            elif new_node.data > curr.data:
                curr = curr.right

            else:
                raise DuplicateKeyError()
        
        if parent.data > new_node.data:
            parent.left = new_node

        elif parent.data < new_node.data:
            parent.right = new_node

        self._size += 1
        return self.root
        

    def search(self, key):
        if self.root is None:
            raise EmptyTreeError()
        
        curr = self.root
        while curr:
            if curr.data == key:
                return True
            
            elif key < curr.data:
                curr = curr.left
            
            else:
                curr = curr.right
        return False



    def delete():
        pass


    # ---------- TRAVERSALS  ----------

    def inorder(self):
        """should return sorted order"""

        result = []

        def recurse(node):
            if node:
                recurse(node.left)
                result.append(node.data)
                recurse(node.right)
            
        recurse(self.root)
        return result

    
    def preorder(self):
        ...         # implement later


    def postorder(self):
        ...         # implement later


    # ---------- UTILITIES ----------

    def find_min():
        pass


    def find_max():
        pass


    def height():
        pass


# ======================================== #


def main():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(12)
    bst.insert(38)
    bst.insert(3)
    bst.insert(20)
    bst.insert(8)
    bst.insert(2)
    print(bst.inorder())
    print(f"found 5? {bst.search(5)}")
    print(f"found 8? {bst.search(8)}")


if __name__ == "__main__":
    main()