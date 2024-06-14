def minIncrementForUnique(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    count = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            diff = nums[i - 1] - nums[i] + 1
            count += diff
            nums[i] = nums[i-1] + 1
    return count

nums = [3,2,1,2,1,7]

print(minIncrementForUnique(nums))
