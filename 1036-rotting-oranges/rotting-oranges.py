class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]

        def valid(r, c):
            return 0<= r< m and 0<= c<n

        fresh = 0
        visited = set()
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        time = -1
        q.append((-1 , - 1))
    
        while q:
            row, col = q. popleft()
            if row == -1:
                time += 1
                if q:
                    q.append((-1, -1))
            else:
                for dx, dy in directions:
                    nextRow, nextCol = row + dx, col + dy
                    if valid(nextRow, nextCol) and grid[nextRow][nextCol] == 1:
                        grid[nextRow][nextCol] = 2
                        q.append((nextRow, nextCol))
                        fresh -= 1
              
        return time if fresh == 0 else -1
 

