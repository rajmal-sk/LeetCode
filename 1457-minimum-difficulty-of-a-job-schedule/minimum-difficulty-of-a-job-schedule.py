class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if len(jobDifficulty) < d:
            return -1
        
        memo = [[float('inf')] * (d + 1) for _ in range(n)]

        def helper(idx, d):
            if d == 1:
                return max(jobDifficulty[idx : ])
            
            if memo[idx][d] != float('inf'):
                return memo[idx][d]
            
            minDiff = float('inf')
            maxEfforts = jobDifficulty[idx]

            for j in range(idx, n - d + 1):
                maxEfforts = max(maxEfforts, jobDifficulty[j])
                memo[idx][d] = min (memo[idx][d] , maxEfforts + helper(j +1, d - 1))
            
            return memo[idx][d]

        return helper(0, d)
        
        
        
        
        