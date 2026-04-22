from core.nodes import TreeNode
from core.exceptions import EmptyTreeError, DuplicateKeyError, KeyNotFoundError

# ======================================== #

class BinarySearchTree():

    def __init__(self):
        self.root = None
        self._size = 0

    
    # ---------- DUNDER METHODS ----------

    def __repr__(self):
        return f"BinarySearchTree({self.inorder()})"

    # ----------

    def __bool__(self):
        return True if self.root else False

    # ----------

    def __iter__(self):
        def recurse(node):
            if node:
                yield from recurse(node.left)
                yield node.data
                yield from recurse(node.right)
        recurse(self.root)

    # ----------

    def __len__(self):
        return self._size

    # ----------

    def __str__(self):
        if self.is_empty():
            return "BST is empty."
        
        return ", ".join(map(str, self.inorder()))


    # ---------- CORE UTILS ----------

    def is_empty(self):
        return True if self.root is None else False

    # ----------

    def size(self):
        return self._size


    # ---------- BASIC OPERATIONS ----------

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
        
    # ----------

    def search(self, key):
        curr = self.root
        while curr:
            if curr.data == key:
                return True
            
            elif key < curr.data:
                curr = curr.left
            
            else:
                curr = curr.right
        return False

    # ----------
    
    def delete(self, val):

        if self.root is None:
            raise EmptyTreeError()
        
        def recurse(node, val):

            if not node:
                raise KeyNotFoundError()            

            if node.data < val:
                node.right = recurse(node.right, val)
                return node
            
            elif node.data > val:
                node.left = recurse(node.left, val)
                return node
            
            else:       # base case for recurse
                
                # CASE 1: delete leaf node
                if node.left is None and node.right is None:
                    self._size -= 1
                    return None

                # CASE 2.1: delete node with only left child
                elif node.right is None:
                    self._size -= 1
                    return node.left
                
                # CASE 2.2: delete node with only right child
                elif node.left is None:
                    self._size -= 1
                    return node.right

                # CASE 3: delete node with both children
                else:
                    # getting the minimum value in right subtree
                    curr = node.right
                    while curr.left:
                        curr = curr.left
                    minm_val = curr.data
                    node.data = minm_val
                    node.right = recurse(node.right, minm_val)
                    return node

        self.root = recurse(self.root, val)

    # ---------- TRAVERSALS ----------

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

    # ----------
    
    def preorder(self):

        """returns tree elements as a list ordered by preorder traversal"""
        result = []
        
        def recurse(node):
            if node:
                result.append(node.data)
                recurse(node.left)
                recurse(node.right)
        
        recurse(self.root)
        return result

    # ----------

    def postorder(self):
        """returns tree elements as a list ordered by postorder traversal"""

        result = []

        def recurse(node):
            if node:
                recurse(node.left)
                recurse(node.right)
                result.append(node.data)
        
        recurse(self.root)
        return result


    # ---------- UTILITIES ----------

    def minm(self):
        if self.root is None:
            raise EmptyTreeError()
        
        curr = self.root
        while curr.left:
            curr = curr.left
        
        return curr.data

    # ----------

    def maxm(self):
        if self.root is None:
            raise EmptyTreeError()
        
        curr = self.root
        while curr.right:
            curr = curr.right

        return curr.data

    # ----------

    def height(self):
        """return the height of bst"""

        def recurse(node):
            if node:
                left_h = recurse(node.left)
                right_h = recurse(node.right)
                return 1 + max(left_h, right_h)
            return -1

        return recurse(self.root)


# ======================================== #


def main():
    bst = BinarySearchTree()
    
    # Insert nodes into the BST
    bst.insert(10)
    bst.insert(12)
    bst.insert(38)
    bst.insert(3)
    bst.insert(20)
    bst.insert(8)
    bst.insert(2)
    bst.insert(11)
    bst.insert(50)
    bst.insert(35)
    
    print("Initial BST (in-order):", bst.inorder())
    print("Initial size:", bst.size())
    
    # Test deleting a leaf node
    print("\nDeleting leaf node 2...")
    bst.delete(2)
    print("BST after deleting 2 (in-order):", bst.inorder())
    print("Size after deleting 2:", bst.size())
    
    # Test deleting a node with one child
    print("\nDeleting node 3 (one child)...")
    bst.delete(3)
    print("BST after deleting 3 (in-order):", bst.inorder())
    print("Size after deleting 3:", bst.size())
    
    # Test deleting a node with two children
    print("\nDeleting node 10 (two children)...")
    bst.delete(10)
    print("BST after deleting 10 (in-order):", bst.inorder())
    print("Size after deleting 10:", bst.size())
    
    # Test deleting a node that does not exist
    print("\nAttempting to delete non-existent node 100...")
    try:
        bst.delete(100)
    except KeyNotFoundError:
        print("KeyNotFoundError: Node 100 does not exist.")
    
    # Test deleting the root node
    print("\nDeleting root node 12...")
    bst.delete(12)
    print("BST after deleting root 12 (in-order):", bst.inorder())
    print("Size after deleting root 12:", bst.size())
    
    # Test deleting all nodes
    print("\nDeleting all nodes...")
    for val in [8, 11, 20, 35, 38, 50]:
        print(f"Deleting {val}...")
        bst.delete(val)
        print("BST (in-order):", bst.inorder())
        print("Size:", bst.size())
    
    print("\nFinal BST (should be empty):", bst.inorder())
    print("Final size (should be 0):", bst.size())




if __name__ == "__main__":
    main()