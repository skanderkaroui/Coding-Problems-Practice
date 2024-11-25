class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stripped_word = ''.join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(stripped_word) - 1
        while l <= r:
            if stripped_word[l] != stripped_word[r]:
                return False
            l += 1
            r -= 1
        return True

obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))


