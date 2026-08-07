class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sorted_prices = sorted(prices)
        i = 0
        profit = 0
        while i < len(prices) - 1:
            j = i + 1
            while j < len(prices):
                profit = max(0, profit , prices[j] - prices[i]) 
                j += 1
            i += 1
        return profit