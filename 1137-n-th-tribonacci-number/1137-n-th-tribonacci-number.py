class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        res = []
        
        for i in range(n+1):
            if i == 0:
                res.append(0)
            elif i <= 2:
                res.append(1)
            else:
                next_number = res[-1] + res[-2] + res[-3]
                res.append(next_number)
        
        return res[n]
        