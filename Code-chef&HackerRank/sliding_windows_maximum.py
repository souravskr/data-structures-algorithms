# def maxSlidingWindow(nums, k: int):
#     initial_sum = sum(nums[:k])
#     res = [initial_sum]
#     for i in range(k):
#         initial_sum = initial_sum - nums[i] + nums[k + i]
#         res.append(initial_sum)
#     return max(res)

# def maxSlidingWindow(nums, k: int):
#     res = []
#     for i in range(len(nums) - k + 1):
#         cur_max = max(nums[i:k + i])
#         res.append(cur_max)
#     return res
#
#
# nums = [1]
# print(maxSlidingWindow(nums, 1))

def sliding_window(s):
    j = max_str = 0
    char_set = set()
    size = len(s)
    for i in range(size):
        while s[i] in char_set:
            char_set.remove(s[j])
            j += 1
        char_set.add(s[i])
        max_str = max(max_str, i - j + 1)

    return max_str


s = "bbbbbb"
print(sliding_window(s))
