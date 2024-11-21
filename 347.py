class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, count in count.items():
            freq[count].append(num)
        
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

            