class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Helper function to check if the neighbor is within bounds and is a land
        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1

        currentArea = [0]

        # Standard way of checking neighbor of a node in a matrix
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(row, col, currentArea):
            for dx, dy in directions:
                nRow, nCol = row + dx, col + dy
                if isValid(nRow, nCol) and (nRow, nCol) not in seen:
                    currentArea[0] += 1 
                    seen.add((nRow, nCol))
                    dfs(nRow, nCol, currentArea)

        
        seen = set()
        maxArea = 0
        for row in range(m):
            for col in range(n):
                currentArea[0] = 0
                if grid[row][col] == 1 and (row, col) not in seen:
                    currentArea[0] += 1
                    seen.add((row,col))
                    dfs(row, col, currentArea)   
                maxArea = max(maxArea, currentArea[0])

        return maxArea

