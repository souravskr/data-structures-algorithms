class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_dict = collections.defaultdict(list)
        n = 0
        while True:
            cur_res = target - nums[n]
            if cur_res not in res_dict:
                res_dict[nums[n]].append(n)
            else:
                res_dict[cur_res].append(n)
                return res_dict[cur_res]

            n += 1
        
        
        
        
        
        # copy_nums = nums.copy()
        # nums.sort()
        # size = len(nums)
        # left = 0
        # right = size - 1
        # result = []
        # while left <= right:
        #     t_sum = nums[left] + nums[right]
        #     if target == t_sum:
        #         first_item = copy_nums.index(nums[left])
        #         second_item = copy_nums.index(nums[right])
        #         if nums[left] == nums[right]:
        #             second_item = copy_nums.index(nums[right], copy_nums.index(nums[left]) + 1)
        #         result.append(first_item)
        #         result.append(second_item)
        #         return result
        #     if t_sum > target:
        #         right -= 1
        #     else:
        #         left += 1