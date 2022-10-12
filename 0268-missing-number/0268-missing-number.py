class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        all_n = [n for n in range(size + 1)]
        return list(set(all_n).difference(set(nums)))[0]