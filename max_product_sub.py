def maxProduct(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        curMin, curMax = 1, 1

        for num in nums:
            curMax, curMin = max(num * curMax, num * curMin, num), min(curMax * num, num * curMin, num)
            res = max(res, curMax)
        return res

print(maxProduct([2,3,-2,4]))