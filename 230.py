# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        res = []
        
        def returnInorder(root):
            if root is None:
                return
            returnInorder(root.left)
            res.append(root.val)
            returnInorder(root.right)

        returnInorder(root)
        
        return res[k-1]