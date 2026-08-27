class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur_buy = prices[0]

        for p in prices:
            max_profit = max(max_profit,p-cur_buy)
            cur_buy = min(p,cur_buy)
        return max_profit