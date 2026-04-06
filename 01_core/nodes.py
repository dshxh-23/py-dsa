class Node:
    """Basic Node structure for singly linked lists"""
    def __init__(self, val, next=None):
        self.data = val
        self.next = next

    def __repr__(self):
        return f"Node({self.data})"

    def __str__(self):
        return f"{self.data}"

    