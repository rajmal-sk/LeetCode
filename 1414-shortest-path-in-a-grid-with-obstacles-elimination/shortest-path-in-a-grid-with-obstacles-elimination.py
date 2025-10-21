class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def valid(row, col):
            return 0<=row<m and 0<=col<n
        
        m = len(grid)
        n = len(grid[0])
        queue = deque([(0, 0, k, 0)])
        seen = {(0, 0, k)}
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while queue:
            r, c, remain, steps = queue.popleft()
            if (r, c) == (m-1, n-1):
                return steps
            
            for dx, dy in directions:
                nRow, nCol = r + dx, c + dy

                if valid(nRow, nCol):
                    if grid[nRow][nCol] == 0 and (nRow, nCol, remain) not in seen: 
                        seen.add((nRow, nCol, remain))
                        queue.append((nRow, nCol, remain, steps + 1))
                    
                    elif remain and (nRow, nCol, remain - 1) not in seen:
                        seen.add((nRow, nCol, remain - 1))
                        queue.append((nRow, nCol, remain - 1, steps + 1))
        
        return -1


