class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        maxSqLen = 0

        dp =[0] * (cols + 1)
        prev = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == "1":
                    dp[j] = min(dp[j-1], prev, dp[j]) + 1
                    maxSqLen = max(maxSqLen, dp[j])
                else:
                    dp[j] = 0
                prev = temp

        return maxSqLen * maxSqLen