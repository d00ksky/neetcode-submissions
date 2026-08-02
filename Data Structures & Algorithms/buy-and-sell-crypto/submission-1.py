class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        for i in range(len(prices)):
            price = prices[i]
            for j in range(i + 1, len(prices)):
                if prices[j] - price > 0:
                    current_profit = prices[j] - price
                    print(current_profit)
                    if profit < current_profit:
                        profit = current_profit
        return profit


            

        