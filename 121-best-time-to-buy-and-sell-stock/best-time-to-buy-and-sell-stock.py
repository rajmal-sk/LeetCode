class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force - For each buy position calculate the max profit.

        # Optimized Solution
        res = 0
        buyIdx = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[buyIdx]:
                res = max(res, prices[i] - prices[buyIdx])
            else:
                buyIdx = i
        return res