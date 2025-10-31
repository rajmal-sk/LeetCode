class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        maxSqLen = 0

        cache = {}

        def recursive(r , c):
            if r >= rows or c >= cols:
                return 0
            
            if (r, c ) not in cache:
                down = recursive(r + 1, c)
                right = recursive(r, c + 1)
                diag = recursive(r + 1, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min (down, right, diag)
            
            return cache[(r, c)]
        
        recursive(0, 0)
        maxSqLen = max(cache.values()) ** 2
        return maxSqLen