class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # size = len(nums)
        # for i in range(size):
        #     val = pow(nums[i], 2)
        #     nums[i] = val
        # nums.sort()
        # return nums
        
        res = collections.deque()
        l_pointer, r_pointer = 0, len(nums) -1

        while l_pointer <= r_pointer:
            left, right = abs(nums[l_pointer]), abs(nums[r_pointer])
            if left > right:
                res.appendleft(pow(left, 2))
                l_pointer += 1
            else:
                res.appendleft(pow(right, 2))
                r_pointer -= 1

        return res