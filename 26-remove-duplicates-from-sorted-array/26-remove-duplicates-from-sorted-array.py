class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        right = 1
        for i in range(1, len(nums)):
            if nums[right] == nums[right - 1]:
                right += 1
            else:
                nums[left] = nums[right]
                left += 1
                right += 1

        return len(nums[:left])