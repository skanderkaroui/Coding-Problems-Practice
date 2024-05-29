def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for index, num in enumerate(nums):
            comp = target - num
            if comp in num_dict:
                return [num_dict[comp],index]
            num_dict[num] = index
        return []

print(twoSum([2,7,11,15],9))