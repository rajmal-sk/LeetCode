class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(n)]

        def dfs(i, holding, remain):
            if i == n or remain == 0:
                return 0
            
            if dp[i][holding][remain] != 0:
                return dp[i][holding][remain]
            
            # We skip the current index
            dp[i][holding][remain] = dfs(i+1, holding, remain)

            # We consider either buying or selling at the current index based on the holding pattern.
            if holding:
                # Only while selling we decrement the counter
                dp[i][holding][remain] = max(dp[i][holding][remain], prices[i] + dfs(i+1, False, remain - 1))
            else:
                # While buying we will not decrement the remaining field
                dp[i][holding][remain] = max(dp[i][holding][remain], -prices[i] + dfs(i+1, True, remain))
            
            return dp[i][holding][remain]
        
        return dfs(0, False, k)