class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # Declare the dp/ memoization array

        dp =[[[-1] * (3) for _ in range(2)] for _ in range(n)]

        def dfs(i, holding, remain):
            if i == n or remain == 0:
                return 0
            
            if dp[i][holding][remain] != -1:
                return dp[i][holding][remain]
            
            # Skip the current index under consideration
            dp[i][holding][remain] = dfs(i+1, holding, remain)

            # Consider the current index and based on the holding pattern take the action

            if holding:
                dp[i][holding][remain] = max(dp[i][holding][remain], prices[i] + dfs(i+1, False, remain - 1)) 
            else:
                dp[i][holding][remain] = max(dp[i][holding][remain], -prices[i] + dfs(i+1, True, remain))

            return dp[i][holding][remain]

        return dfs(0, False, 2) 