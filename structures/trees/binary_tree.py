from structures.nodes import TreeNode
from core.exceptions import TreeError

from structures.queue.linked_queue import LinkedQueue

# ======================================== #

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self._size = 0 if root is None else 1


    # ---------- BASIC ----------
    
    def is_empty(self):
        """return true if tree is empty"""
        return self.root is None

    def size(self):
        """return size of tree"""
        return self._size

    def get_root(self):
        """return root of tree"""
        return self.root

    def set_root(self, val):
        """initialize tree with root node"""
        if self._size != 0:
            raise TreeError("Tree already has a root!")
        
        self.root = TreeNode(val)
        self._size = 1

    
    # ---------- OPERATIONS ----------

    def insert(self, val):
        """insert val into tree, using level-order insertion to keep tree complete"""

        new_node = TreeNode(val)

        # case 1: insert in empty tree
        if self.root is None:
            self.root = new_node
            self._size = 1
            return
        
        # case 2: insert in tree
        q = LinkedQueue()
        q.enqueue(self.root)

        while not q.is_empty():
            curr = q.dequeue()
            
            if curr.left is None:
                curr.left = new_node # insert as left child
                self._size += 1
                return
            
            if curr.right is None:
                curr.right = new_node # insert as right child
                self._size += 1
                return

            # if unable to insert, enqueue left and right child
            q.enqueue(curr.left)
            q.enqueue(curr.right)


    # ---------- TRAVERSAL ----------

    def preorder(self):
        """traverse tree using preorder (data, left, right) traversal"""

        result = []

        def recurse(node):
            if node:
                result.append(node.data)
                recurse(node.left)
                recurse(node.right)

        recurse(self.root)
        return result

    
    def inorder(self):
        """traverse tree using inorder (left, data, right) traversal"""
        
        result = []

        def recurse(node):
            if node:
                recurse(node.left)
                result.append(node.data)
                recurse(node.right)

        recurse(self.root)
        return result


    def postorder(self):
        """traverse tree using postorder (left, right, data) traversal"""
        
        result = []

        def recurse(node):
            if node:
                recurse(node.left)
                recurse(node.right)
                result.append(node.data)
        
        recurse(self.root)
        return result


    def level_order(self):
        """traverse tree using level-order traversal"""

        result = []
        q = LinkedQueue()
        q.enqueue(self.root)

        while not q.is_empty():
            curr = q.dequeue()
            if curr:
                result.append(curr.data)
                q.enqueue(curr.left)
                q.enqueue(curr.right)
            
        return result

    
    # ---------- UTILS ----------

    def search(self, key):
        """return true if key exists"""

        if self.root is None:
            return False

        q = LinkedQueue()
        q.enqueue(self.root)

        while not q.is_empty():
            curr = q.dequeue()

            if curr.data == key:
                return True

            if curr.left:
                q.enqueue(curr.left)

            if curr.right:
                q.enqueue(curr.right)

        return False 


    def height(self):
        """return height of tree, -1 for empty tree and 0 for tree with only root node"""
        def _height(node):
            if node is None:
                return -1

            left_height = _height(node.left)
            right_height = _height(node.right)
            return 1 + max(left_height, right_height)

        return _height(self.root)


    # ---------- DUNDER METHODS ----------

    def __repr__(self):
        pass


    def __bool__(self):
        return True if self.root is not None else False


    def __iter__(self):
        q = LinkedQueue
        q.enqueue(self.root)
        while not q.is_empty():
            curr = q.dequeue
            if curr:
                yield curr.data
                q.enqueue(curr.left)
                q.enqueue(curr.right)


    def __len__(self):
        return self._size


    def __str__(self):
        """simple level-order print"""
        if self.root is None:
            return f"tree is empty!"

        q = LinkedQueue()
        q.enqueue(self.root)
        node_vals = []
        while not q.is_empty():
            curr = q.dequeue()

            if curr:
                node_vals.append(str(curr.data))
                q.enqueue(curr.left)
                q.enqueue(curr.right)
        
        return f"Tree (Level Order Traversal): {' '.join(node_vals)}"


# ======================================== #


def main():
        t = BinaryTree()
        t.insert(1)
        t.insert(2)
        t.insert(3)
        t.insert(4)
        t.insert(5)
        t.insert(6)
        t.insert(7)
        t.insert(8)
        t.insert(9)
        
        print(t)
        print(t.inorder())
        print(t.preorder())
        print(t.postorder())
        print(t.level_order())
        print("5 in tree? " + str(t.search(5)))
        print("11 in tree? " + str(t.search(11)))
        print(f"height: {t.height()}")

if __name__ == "__main__":
        main()