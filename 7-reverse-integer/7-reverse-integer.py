class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        min = - int(math.pow(2, 31))
        max = int(math.pow(2, 31) -1)
        while x:
            left = int(math.fmod(x, 10))
            x = int(x/10)
            res = res * 10 + left
        if res < min or res > max:
            return 0
        return res
        