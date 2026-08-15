class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_buy = prices[0]
        max_profit = 0

        for p in prices:
            cur_buy = min(cur_buy,p)
            max_profit = max(max_profit,p - cur_buy)
        return max_profit