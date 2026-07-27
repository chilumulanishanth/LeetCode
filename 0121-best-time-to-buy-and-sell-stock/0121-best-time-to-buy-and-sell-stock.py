class Solution(object):
    def maxProfit(self, prices):
        profit=0
        buy=prices[0]
        for i in range(len(prices)):
            current_profit=prices[i]-buy
            if current_profit>profit:
                profit =current_profit
            if buy>prices[i]:
                buy=prices[i]     
        return(profit)
        