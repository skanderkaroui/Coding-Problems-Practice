# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def checkBST(root, left, right):
            if not root:
                return True
            if not (left < root.val < right):
                return False
            
            return (checkBST(root.left, left, root.val) and 
                    checkBST(root.right, root.val, right))
            
        
        return checkBST(root, float('-inf'), float('inf'))