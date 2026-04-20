class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        l = 0
        r = 1
        while (r < len(prices)):
            if prices[l] < prices[r]:
                a = prices[r] - prices[l]
                total = max(total, a)
            else:
                l = r
            r += 1
        return total