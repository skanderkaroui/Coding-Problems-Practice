class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res += self.inorderTraversal(root.right)
        return res
    
    def PreorderTraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res += self.PreorderTraversal(root.left)
            res += self.PreorderTraversal(root.right)
        return res
    
    def PostorderTraversal(self,root):
        res = []
        if root:
            res = self.PreorderTraversal(root.left)
            res += self.PreorderTraversal(root.right)
            res.append(root.data)
            return res

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.printTree()
print(root.inorderTraversal(root))
print(root.PreorderTraversal(root))
print(root.PostorderTraversal(root))