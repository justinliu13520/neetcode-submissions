class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        bestBuy = prices[0] #starting point

        for sell in prices:
            maxP = max(maxP,sell-bestBuy)
            bestBuy = min(sell,bestBuy)
        return maxP