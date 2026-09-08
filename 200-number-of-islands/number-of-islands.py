class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        row, col = len(grid), len(grid[0])
        island = 0

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != "1":
                return 
            grid[r][c] = "0"
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
            
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    island += 1
                    dfs(r, c)
        return island