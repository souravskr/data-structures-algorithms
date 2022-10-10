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


def fibo(n):
    if n <= 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


def fibo_iterative(n):
    res = []
    for i in range(n):
        if i == 0 or i == 1:
            res.append(1)
        else:
            last_item = res[-1] + res[-2]
            res.append(last_item)
    return res[-1]


print(fibo_iterative(40))
print(fibo(40))
