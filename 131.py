class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        subset = []
        res = []

        def isPalindrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(i, subset):
            if i == len(s):
                res.append(list(subset))
                return
            
            for j in range(i + 1, len(s) + 1):
                part = s[i:j]
                if isPalindrome(part):
                    subset.append(part)
                    dfs(j, subset)
                    subset.pop()

        dfs(0, [])
        return res
