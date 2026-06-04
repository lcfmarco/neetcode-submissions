class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max = 0
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            curr_max = max(curr_max, price - lowest)
        return curr_max