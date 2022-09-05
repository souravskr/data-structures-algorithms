class Solution:
    def climbStairs(self, n: int) -> int:
        res = []
        for i in range(n+1):
            if i <= 1:
                res.append(1)
            else:
                next_item = res[-1] + res[-2]
                res.append(next_item)
        return res[-1]