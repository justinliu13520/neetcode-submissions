class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        cheapestBuy = float("inf")

        for p in prices:
            cheapestBuy = min(p,cheapestBuy)
            maxP = max(maxP,p-cheapestBuy)

        return maxP
