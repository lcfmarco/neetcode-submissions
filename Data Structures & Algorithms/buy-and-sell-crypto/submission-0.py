class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > curr_max:
                    curr_max = prices[j] - prices[i]
        return curr_max