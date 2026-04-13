from core.nodes import TreeNode
# import tree exceptions also
from data_structures.queue.linked_queue import LinkedQueue

class BinaryTree:
    
    # ---------- DUNDER METHODS ----------
    def __init__(self, root=None):
        self.root = root
        self._size = 0 if root is None else 1

    def __repr__(self):
        pass

    def __bool__(self):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def __str__(self):
        """simple level-order print"""
        if self.root is None:
            return f"tree is empty!"

        q = LinkedQueue()
        q.enqueue(self.root)
        node_vals = []
        while not q.is_empty():
            curr = q.dequeue()
            node_vals.append(str(curr.data))

            if curr.left is not None:
                q.enqueue(curr.left)
            
            if curr.left is not None:
                q.enqueue(curr.right)
        
        return f"Level order traversal: {' '.join(node_vals)}"
            

    
    # ---------- BASIC OPERATIONS ----------
    
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
        """set val as root of tree"""
        pass

    
    # ----------  ----------

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

    def preorder(self):
        """traverse tree uusing preorder traversal"""
        pass
    
    def inorder(self):
        """traverse tree uusing inorder traversal"""
        pass

    def postorder(self):
        """traverse tree using postorder traversal"""
        pass

    def level_order(self):
        """traverse tree using level-order traversal"""
        pass

    
    def search(self, key):
        """return true if key exists"""
    

    def height(self):
        """return height of tree"""



#=================================================================================================== 


def main():
        t = BinaryTree()
        t.insert(10)
        t.insert(20)
        t.insert(30)
        print(t)

if __name__ == "__main__":
        main()