class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def valid(row, col):
            return 0 <= row < n and 0<= col < n and grid[row][col] == 0
        
        n = len(grid)
        seen = {(0,0)}
        queue = deque([(0, 0, 1)])

        while queue:
                row, col, steps = queue.popleft()
                if row == n-1 and col == n-1:
                    return steps
  
                for dx, dy in directions:
                    nRow , nCol = row+dx, col+dy
                    if valid(nRow, nCol) and (nRow, nCol) not in seen:
                        seen.add((nRow, nCol))
                        queue.append((nRow, nCol, steps + 1))

        return -1

        