def is_bst(root):

    if not root:
        return True

    def tree_lesser(tree_root, val):
        if not tree_root:
            return True
            
        return (tree_root.data < val and 
                tree_lesser(tree_root.left, val) and 
                tree_lesser(tree_root.right, val))

    
    def tree_greater(tree_root, val):
        if not tree_root:
            return True
            
        return (tree_root.data > val and 
                tree_greater(tree_root.left, val) and 
                tree_greater(tree_root.right, val)) 


    return (is_bst(root.right) and 
            is_bst(root.left) and
            tree_lesser(root.left, root.data) and 
            tree_greater(root.right, root.data))