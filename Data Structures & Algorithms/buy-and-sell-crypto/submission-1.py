class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = [101]*len(prices)
        best_sell = [-1]*len(prices)
        
        best_buy[0] = prices[0]
        best_sell[len(prices)-1] = prices[len(prices)-1]

        for i in range(1,len(prices)):
            if best_buy[i-1] < prices[i]:
                best_buy[i] = best_buy[i-1]
            else:
                best_buy[i] = prices[i]
        
        for j in range(len(prices)-2,-1,-1):
            if best_sell[j+1] > prices[j]:
                best_sell[j] = best_sell[j+1]
            else:
                best_sell[j] = prices[j]
        highest_profit = 0
        for k in range(len(prices)-1):
            if prices[k] > best_sell[k]:
                continue
            if best_sell[k] - best_buy[k] > highest_profit:
                highest_profit = best_sell[k] - best_buy[k]
        return highest_profit