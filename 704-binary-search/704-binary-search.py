class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        left = 0
        right = size - 1
        
        while left <= right:
            mid = int((left + right) / 2)
            
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return -1 