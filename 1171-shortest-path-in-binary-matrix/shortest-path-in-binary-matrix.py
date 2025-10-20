class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        visited = set()

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def valid(row, col):
            return 0 <= row < n and 0<= col < n and grid[row][col] == 0
        
        n = len(grid)
        depth = 0
        queue = deque([(0,0)])

        while queue:
            k = len(queue)
            for _ in range(k):
                l = queue.popleft()
                row, col = l[0], l[1]
                if (row, col) not in visited:
                    if row == n-1 and col == n-1:
                        depth += 1
                        return depth
    
                    visited.add((row, col))
                    for dx, dy in directions:
                        nRow , nCol = row+dx, col+dy
                        if valid(nRow, nCol):
                            queue.append((nRow, nCol))

            depth += 1

        return -1

        