class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        b = prices[0]

        for i in range(1, len(prices)):
            s = prices[i]
            if b > s:
                b = s
            p = max(p, s - b)
            if i < len(prices) -1:
                s = prices[i + 1]
        return p
        