class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def isvalid(row, col):
            return 0<= row < m and 0<= col < n and grid[row][col] == "1"

        def dfs(row, col):
            for dx, dy in directions:
                nextrow, nextcol = row + dx, col + dy
                if isvalid(nextrow, nextcol) and (nextrow, nextcol) not in seen:
                    seen.add((nextrow, nextcol))
                    dfs(nextrow, nextcol)
        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row, col) not in seen:
                    count += 1
                    seen.add((row,col))
                    dfs(row, col)
        
        return count