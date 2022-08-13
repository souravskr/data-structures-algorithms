class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            if i < size:
                count = nums[i:].count(nums[i])
                if count > 2:
                    for j in range(len(nums[i: i + count]) -1):
                        print(nums[i: count])
                        nums.pop(i + 1)
                    size = len(nums)
                elif count > 1:
                    nums.pop(i)
                    size = len(nums)
        return len(nums)
