class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Window method

        l, r = 0, 1

        # Idea: As long as the left price is smaller than the right, we calculate profit
        # Otherwise, we make l = r, because that means we have found a new low price to purchase
            # We still keep track of max profit as we go, so even if the max profit is still higher before
            # the new low buy point, we can still return it
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return max_profit

