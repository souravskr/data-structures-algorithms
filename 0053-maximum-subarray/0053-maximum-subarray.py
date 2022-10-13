class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's Algorithm
        res = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
            res = max(res, nums[i])
        return res
    
    
        # c_sum = nums[0]
        # g_sum = nums[0]
        # for i in range(1, len(nums)):
        #     c_sum = max(nums[i], c_sum + nums[i])
        #     if c_sum > g_sum:
        #         g_sum = c_sum
        # return g_sum