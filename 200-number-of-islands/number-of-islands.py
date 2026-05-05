class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"
            
        count = 0

        def dfs(row, col):
            for dx, dy in directions:
                nrow, ncol = row + dx, col + dy
                if isValid(nrow, ncol) and (nrow, ncol) not in seen:
                    seen.add((nrow, ncol))
                    dfs(nrow, ncol)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row, col) not in seen:
                    count += 1
                    seen.add((row, col))
                    dfs(row, col)
        
        return count