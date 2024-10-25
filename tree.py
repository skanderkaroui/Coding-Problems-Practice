class BinaryTree:
    def __init__(self, node):
        self.val = val
        self.left = None
        self.right = None
    
    def inorderTraversal(self, root):
        if not root:
            return
        self.inorderTraversal(root.left)
        print(root.val)
        self.inorderTraversal(root.right)