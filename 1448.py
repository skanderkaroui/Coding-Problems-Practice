# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.count = 0

        def dfs(root, maxGood):            
            if root.val >= maxGood:
                self.count += 1
            maxGood = max(maxGood, root.val)
            
            if root.left:
                dfs(root.left, maxGood)
            if root.right:
                dfs(root.right, maxGood)
        
        dfs(root, root.val)

        return self.count