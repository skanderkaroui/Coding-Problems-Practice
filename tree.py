class BinaryTree:
    def __init__(self, node):
        self.val = val
        self.left = None
        self.right = None
    
    def insert_right(self, val):
        if self.right is None:
            self.right = BinaryTree(val)
        else:
            newNode = BinaryTree(val)
            newNode.right = self.right
            self.right = newNode
    
    def pre_order(self):
        print(self.val)

        if self.left:
            self.left.pre_order()
        
        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self.left:
            self.left.in_order()
        
        print(self.val)

        if self.right:
            self.right.in_order()

    def BFS(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            print(current_node.val)

            if current_node.left:
                queue.put(current_node.left)

            if current_node.right:
                queue.put(current_node.right)
