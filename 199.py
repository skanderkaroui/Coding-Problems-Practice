# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Queue import Queue
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        res = []
        q = Queue()
        q.put(root)

        while not q.empty():
            level_size = q.qsize()

            for i in range(level_size):
                current_node = q.get()
                
                if i == level_size - 1:
                    res.append(current_node.val)
            
                if current_node.left:
                    q.put(current_node.left)
                    
                if current_node.right:
                    q.put(current_node.right)

        return res