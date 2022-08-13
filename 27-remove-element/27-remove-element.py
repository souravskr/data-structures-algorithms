class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            index = nums.index(val)
            nums.pop(index)
        return len(nums)