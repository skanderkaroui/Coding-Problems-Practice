class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        subset = []
        candidates.sort()
        
        def dfs(i, total):
            if total == target:
                res.append(subset[:])
                return
            if total > target or i >= len(candidates):
                return
            
            subset.append(candidates[i])
            dfs(i+1, total+ candidates[i])
            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(i+1, total)
        
        dfs(0, 0)
        return res
    
obj = Solution()
print(obj.combinationSum2([10,1,2,7,6,1,5],8))
print(obj.combinationSum2([2,5,2,1,2],5))