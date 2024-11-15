class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def isAnagram(s, t):
            if len(s) != len(t):
                return False
            
            count = [0] * 26

            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1
                count[ord(t[i]) - ord('a')] -= 1
            
            for val in count:
                if val != 0:
                    return False
            return True
        
        res = []
        subset = []

        for i in range(len(strs)):
            subset.append[strs[i]]
            if strs[i] not in res:
                for j in range(i + 1, len(strs)):
                    if isAnagram(strs[i], strs[j]):
                        subset.append(strs[j])
                res.append(subset)
                subset = []
        return res
                    
obj = Solution()
print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(obj.groupAnagrams(['']))
print(obj.groupAnagrams([["a"]]))
