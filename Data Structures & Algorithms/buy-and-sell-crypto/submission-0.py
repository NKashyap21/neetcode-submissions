class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,1
        max_profit = 0
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit < 0:
                profit = 0
                buy = sell 
            else:
                max_profit = max(profit,max_profit)
                sell += 1
        return max_profit
        
