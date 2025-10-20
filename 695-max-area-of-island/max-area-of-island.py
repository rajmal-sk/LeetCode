class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = 0
        seen = set()

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1 and (row, col) not in seen

        def dfs(row, col):
            if not valid(row, col):
                return 0
            seen.add((row, col))
            return 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in seen:
                    ans = max(ans, dfs(row, col))

        return ans

