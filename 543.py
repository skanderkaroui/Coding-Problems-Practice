# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            
            right = dfs(curr.right)
            left = dfs(curr.left)

            self.res = max(self.res, right + left)

            return 1 + max(right, left)
        
        dfs(root)
        return self.res