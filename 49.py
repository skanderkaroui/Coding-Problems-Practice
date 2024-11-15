class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in res:
                res[sorted_word] = []
            res[sorted_word].append(word)
        
        return list(res.values())

                    
obj = Solution()
print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(obj.groupAnagrams(['']))
print(obj.groupAnagrams([["a"]]))
