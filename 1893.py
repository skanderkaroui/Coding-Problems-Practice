class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = [False] * 51

        for start, end in ranges:
            for num in range(start, end + 1):
                covered[num] = True
        
        for num in range(left, right + 1):
            if not covered[num]:
                return False
        
        return True
