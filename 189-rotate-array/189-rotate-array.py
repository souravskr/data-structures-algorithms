class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for _ in range(k):
        #     last = nums.pop()
        #     nums.insert(0, last)
        
        size = len(nums)
        k = k % size
        self.reverse(nums, 0, size - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, size - 1)
        
    
    
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums
        
        