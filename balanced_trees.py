class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data
    
    def insert(self,data):
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

    def is_balanced(self):
        if self.data:
            if self.left and self.right:
                is_balanced(self.data)  
        if (self.data - self.left == 1) or (self.right - self.data == 1):
            return True
        else:
            return False

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.balanced(root))
                
            