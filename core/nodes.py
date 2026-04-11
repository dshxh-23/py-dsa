class Node:
    """Basic Node structure for singly linked lists"""
    def __init__(self, val, next=None):
        self.data = val
        self.next = next

    def __repr__(self):
        return f"Node({self.data})"

    def __str__(self):
        return f"{self.data}"


class TreeNode:
    """basic node structure for trees with 2 children"""
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.data})"
    
    def __str__(self):
        return f"{self.data}"

    def is_leaf(self):
        return self.left is None and self.right is None