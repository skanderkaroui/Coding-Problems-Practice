class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        l = 0
        max_len = 0
        char_set = set()

        for r, char in enumerate(s):
            while char in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(char)
            max_len = max(max_len, r - l + 1)
        
        return max_len