class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
    
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         for i in set(nums):
#             if nums.count(i) == 1:
#                 return i
                
                
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         for k, v in collections.Counter(nums).items():
#             if v == 1:
#                 return k 
        