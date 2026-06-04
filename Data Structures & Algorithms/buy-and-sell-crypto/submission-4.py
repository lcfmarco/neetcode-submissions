class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding window problem

        max_profit = 0

        min_sofar = prices[0]


        for i in prices:
            if min_sofar > i:
                min_sofar = i

            profit = i - min_sofar

            if profit > max_profit:
                max_profit = profit

        return max_profit

