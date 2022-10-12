class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        j = 0
        m = nums[j]
        for n in range(1, len(nums)):
            if m == nums[n]:
                return nums[n]
            j += 1
            m = nums[j]
            
            