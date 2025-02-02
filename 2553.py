class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for num in nums:
            num_list = list(str(num))
            for i in range(len(num_list)):
                res.append(int(num_list[i]))
        
        return res