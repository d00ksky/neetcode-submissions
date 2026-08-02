class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day = 0
        max_profit = 0
        for day in range(len(prices)):
            for price in prices[day:]:
                print(f"day = {day}")
                print(f"prices[day] = {prices[day]}")
                print(f"price = {price}")
                if price > prices[day]:
                    print("eureka")
                    profit = price - prices[day]
                    if max_profit < profit:
                        max_profit = profit
                        print(max_profit)
                else:
                    print("nope")
        return max_profit