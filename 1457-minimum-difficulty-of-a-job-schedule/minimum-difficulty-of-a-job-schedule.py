class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if len(jobDifficulty) < d:
            return -1
        
        # memo[d][i] - minimum efforts required to complete the first i task in d days
        memo = [[float('inf')] * (n + 1) for _ in range(d + 1)]
        memo[0][0] = 0
        for deadline in range(1, d + 1):
            for i in range(1, n + 1):
                maxEffort = 0
                for j in range(i -1, deadline - 2, - 1):
                    maxEffort = max(maxEffort, jobDifficulty[j])
                    memo[deadline][i] = min(memo[deadline][i], maxEffort + memo[deadline - 1][j])


        return memo[d][n]
        
        
        
        
        