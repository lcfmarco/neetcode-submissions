class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        # left is the buy point, right is the sell point

        maxProfit = 0

        # While we haven't looped through all the prices yet
        while r < len(prices): 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                # Otherwise, we have found a lower price for the buy point
                # that comes after the day of the current buy point
                l = r # the new buy point becomes the new sell point we found 
            
            r = r + 1
        return maxProfit
