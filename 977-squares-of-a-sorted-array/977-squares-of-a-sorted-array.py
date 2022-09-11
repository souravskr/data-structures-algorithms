class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for i in range(size):
            val = pow(nums[i], 2)
            nums[i] = val
        nums.sort()
        return nums
        