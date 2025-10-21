class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        sRow, sCol = None, None
        # Step 1: Find my location
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    sRow, sCol = i, j
                    break
        
        seen = {(sRow, sCol)}
        queue = deque([(sRow, sCol, 0)])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        while queue:
            r, c, step = queue.popleft()
            if grid[r][c] == "#":
                return step
            
            for dx, dy in directions:
                nRow, nCol = r + dx, c + dy
                if valid(nRow, nCol) and (nRow, nCol) not in seen:
                    if grid[nRow][nCol] != "X":
                        seen.add((nRow, nCol))
                        queue.append((nRow, nCol, step + 1))


        return -1
       # Step 2: Find the closest food cell by doing BFS
