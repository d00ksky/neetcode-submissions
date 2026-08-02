class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        lowest_price = prices[0]

        for price in prices[1:]:
            if price < lowest_price:
                lowest_price = price
            else:
                profit_new = price - lowest_price
                if profit_new > profit:
                    profit = profit_new
        return profit

            

        