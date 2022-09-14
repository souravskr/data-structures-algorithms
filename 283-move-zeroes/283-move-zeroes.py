class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast = 0
        for slow in range(len(nums)):
            if nums[slow] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                fast += 1
        return nums
