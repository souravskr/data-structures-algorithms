import collections


class Solution:
    def two_sum(self, nums, target):
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


new_sol = Solution()
nums = [2, 7, 11, 15]
target = 9

print(new_sol.two_sum(nums, target))
