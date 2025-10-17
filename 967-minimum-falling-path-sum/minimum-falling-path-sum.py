class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = [[None for _ in range(n)] for _ in range(n)]
        minPath = float('inf')

        def dfs(row, col):
            if col < 0 or col == n:
                return float('inf')
            if row == n - 1:
                return matrix[row][col]
            if memo[row][col] != None:
                return memo[row][col]
            
            memo[row][col] = matrix[row][col] + min(dfs(row+1, col-1),dfs(row+1, col), dfs(row+1, col+1))
            return memo[row][col]

        for col in range(n):
            minPath = min(minPath, dfs(0,col))
        
        return minPath