class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = j = 0
        profit = 0
        for k in range(1, len(prices)):
            if prices[k] > prices[i] and prices[k] > prices[j]:
                j += 1
            elif prices[k] > prices[i] and prices[k] < prices[j]:
                profit += (prices[j] - prices[i])
                j = i = k
            elif prices[k] <= prices[i] or prices[k] <= prices[j]:
                profit += (prices[j] - prices[i])
                j = i = k
        profit += (prices[j] - prices[i])
        return profit