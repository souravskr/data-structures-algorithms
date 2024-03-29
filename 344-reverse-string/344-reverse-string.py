class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        right = len(s) -1
        mid = (len(s) // 2)
        for left in range(mid):
            # print(left)
            s[left], s[right] = s[right], s[left]
            right -= 1
        # left = 0
        # right = len(s) -1
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1
        