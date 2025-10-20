class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        matrix = [row[:] for row in mat]
        seen = set()
        queue= deque([])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    seen.add((i, j))
        
        def valid(row, col):
            return 0<=row<m and 0<=col<n
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col, depth = queue.popleft()
            for dx, dy in directions:
                nextRow, nextCol = row + dx, col + dy
                # All the zeroes would be already in the seen and this wil pass only when it is 1
                if valid(nextRow, nextCol) and (nextRow, nextCol) not in seen:
                    seen.add((nextRow, nextCol))
                    queue.append((nextRow, nextCol, depth + 1))
                    matrix[nextRow][nextCol] = depth + 1
        
        return matrix
