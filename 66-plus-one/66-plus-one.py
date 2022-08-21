class Solution:
    def plusOne(self, arr: List[int]) -> List[int]:
        arr_string = [str(i) for i in arr]
        arr_string = int(''.join(arr_string))
        arr_string += 1
        res = [int(n) for n in str(arr_string)]
        # res = []
        # while arr_string:
        #     right = arr_string % 10
        #     res.append(right)
        #     arr_string = arr_string // 10
        # res.reverse()
        return res