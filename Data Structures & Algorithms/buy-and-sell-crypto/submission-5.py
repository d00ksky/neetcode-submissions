class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        lowest_price = prices[0]

        for i in range(len(prices)):
            if prices[i] - lowest_price > profit:
                profit = prices[i] - lowest_price
            if prices[i] < lowest_price:
                lowest_price = prices[i]
        return profit
