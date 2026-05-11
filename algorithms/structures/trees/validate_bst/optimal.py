def is_bst(root):

    def chk_root(node, low, high):
        if not node:
            return True
            
        return (
            low < node.data < high and
            chk_root(node.left, low, node.data) and
            chk_root(node.right, node.data, high)
        )
    
    return chk_root(root, float('-inf'), float('inf'))