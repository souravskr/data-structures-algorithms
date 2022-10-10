# Solution 2 -->  O(n)
def sum_on2(nums):
    # Todo: if array is empty, return 0
    if len(nums) == 0:
        return 0
    # Todo: Slice and sum after that
    rest = nums[1:]
    return nums[0] + sum_on2(rest)


print(sum_on2([1, 2, 3, 4]))


# Solution 2 -->  O(n)
def helper(nums, index):
    if index == len(nums):
        return 0
    return nums[index] + helper(nums, index + 1)


def arr_sum(nums, index=0):
    return helper(nums, index)


print(arr_sum([1, 2, 3, 4]))
