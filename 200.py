class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        seen = set()
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < n and 0 <= j < m and grid[i][j] == '1' and (i,j) not in seen:
                seen.add((i,j))
                dfs(i - 1, j) 
                dfs(i + 1, j) 
                dfs(i, j - 1) 
                dfs(i, j + 1)
                return True
            return False

        for i in range(n):
            for j in range(m):
                if dfs(i, j):
                    count += 1
        
        return count