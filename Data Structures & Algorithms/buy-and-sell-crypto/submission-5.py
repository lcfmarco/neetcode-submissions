class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP Method

        max_profit = 0

        low_buy = prices[0]

        for price in prices:
            max_profit = max(max_profit, price - low_buy)
            low_buy = min(price, low_buy)

        return max_profit


