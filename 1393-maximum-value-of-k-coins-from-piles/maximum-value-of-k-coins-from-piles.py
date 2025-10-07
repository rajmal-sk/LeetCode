class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[-1] * (k+1) for _ in range(n)]
        
        # len(piles) * k calls - even more than that but cache will be hit and retruned immediately.
        # But the other times there is a loop and assuming each pile has an average length of x
        # TC = len(piles) * k * x
        def dfs(i, remain):
            # Base Case:
            if i == n:
                return 0
            
            if dp[i][remain] != -1:
                return dp[i][remain]
            
            # Skip the current pile
            dp[i][remain] = dfs(i+1, remain)
            currPileSum = 0

            # Check all the possibilities of the current pile
            for j in range(min(len(piles[i]), remain)):
                currPileSum += piles[i][j]
                dp[i][remain] = max(dp[i][remain], currPileSum + dfs(i+1, remain - j - 1)) # j - 1 because j starts at 0
            
            return dp[i][remain]



        return dfs(0, k)