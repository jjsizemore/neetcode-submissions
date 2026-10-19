class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = math.inf
        profit = 0

        for i in range(len(prices)):
            profit = max(profit, prices[i] - lowest)
            lowest = min(lowest, prices[i])

        return profit
