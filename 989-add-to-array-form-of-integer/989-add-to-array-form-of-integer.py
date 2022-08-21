class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = int(''.join([str(i) for i in num]))
        pre_res = num + k
        res = []
        while pre_res:
            end_digit = pre_res % 10
            res.append(end_digit)
            pre_res = pre_res // 10
        res.reverse()
        return res