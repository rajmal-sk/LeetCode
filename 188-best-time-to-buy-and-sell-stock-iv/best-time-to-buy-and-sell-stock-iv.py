class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[float('-inf')] * (k + 1) for _ in range(2)] for _ in range(n)]

        def dfs(i, holding, remain):
            if i == n or remain == 0:
                return 0
            
            if dp[i][holding][remain] != float('-inf'):
                return dp[i][holding][remain]
            
            dp[i][holding][remain] = dfs(i+1, holding, remain)

            if holding:
                dp[i][holding][remain] = max(dp[i][holding][remain], prices[i] + dfs(i+1, False, remain - 1))
            else:
                dp[i][holding][remain] = max(dp[i][holding][remain], -prices[i] + dfs(i+1, True, remain))
            
            return dp[i][holding][remain]
        
        return dfs(0, False, k)