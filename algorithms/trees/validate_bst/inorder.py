def is_bst(root):
    if not root: 
        return True

    prev = float('-inf')

    def inorder(node):
        nonlocal prev

        if not node:
            return True

        if not inorder(node.left):
            return False

        if node.data <= prev:
            return False
        
        prev = node.data

        return inorder(node.right)

    return inorder(root)  