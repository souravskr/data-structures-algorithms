class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c_sum = nums[0]
        g_sum = nums[0]
        for i in range(1, len(nums)):
            c_sum = max(nums[i], c_sum + nums[i])
            if c_sum > g_sum:
                g_sum = c_sum
        return g_sum