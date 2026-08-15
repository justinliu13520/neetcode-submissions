class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        bestBuy = prices[0] #starting point

        for sell in prices:
            maxP = max(maxP,sell-bestBuy) #see if selling is more profit
            # it is sell - bestBuy because we dont want to buy in the future and sell in the past
            # bestBuy is from the past and the sell is now.
            bestBuy = min(sell,bestBuy) #if the current price is smaller buy and see if greater profit possible
        return maxP