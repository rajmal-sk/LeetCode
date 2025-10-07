class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        
        # Memoization
        dp = [[-1] * 2 for _ in range(n)]
        
        def dfs(i, holding):
            
            # Base Case: Reaching end of the prices list.
            if i == n:
                return 0
            
            # Check if the sub problem is already solved
            if dp[i][holding] != -1:
                return dp[i][holding]
            
            # Skipping the current index scenario
            dp[i][holding] = dfs(i + 1, holding)
            
            # Considering the current index scenario. 
            # Selling if already holding else buying if not holding anything
            if holding:
                dp[i][holding] = max(dp[i][holding], prices[i] + dfs(i+1, False) - fee)
            else:
                dp[i][holding] = max(dp[i][holding], -prices[i] + dfs(i+1, True))
            
            return dp[i][holding]
        
        return dfs(0, False)