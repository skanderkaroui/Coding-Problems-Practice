class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        pos = {num: index for index, num in enumerate(nums)}

        for old, new in operations:
            index_old = pos[old]
            nums[index_old] = new
            pos[new] = index_old
            del pos[old]
        
        return nums
    