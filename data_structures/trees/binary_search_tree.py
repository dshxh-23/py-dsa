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
        return f"BinarySearchTree({self.inorder()})"


    def __bool__(self):
        return True if self.root else False


    def __iter__(self):
        def recurse(node):
            if node:
                recurse(node.left)
                yield node.data
                recurse(node.right)
        recurse(self.root)


    def __len__(self):
        return self._size


    def __str__(self):
        if self.is_empty():
            return " BST is empty."
        
        return ", ".join(map(str, self.inorder()))


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
        pass        # implement later


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

    def find_min(self):
        if self.root is None:
            raise EmptyTreeError()
        
        curr = self.root
        while curr.left:
            curr = curr.left
        
        return curr.data



    def find_max(self):
        if self.root is None:
            raise EmptyTreeError()
        
        curr = self.root
        while curr.right:
            curr = curr.right

        return curr.data


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
    print(bst)
    print(f"found 5? {bst.search(5)}")
    print(f"found 8? {bst.search(8)}")
    print(f"minimum element: {bst.find_min()}")
    print(f"maximum element: {bst.find_max()}")


if __name__ == "__main__":
    main()