class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums)
        if len(my_set) == len(nums):
            return False
        return True
        