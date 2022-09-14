import collections


def angry_professor(k, a):
    on_time = 0
    for i in a:
        if i <= 0:
            on_time += 1
    print(on_time)
    if on_time >= k:
        return 'YES'
    return 'NO'


arr = [-1, -3, 4, 2]
k = 3


# print(angry_professor(k, arr))


def merge(nums1, m, nums2, n):
    i = (m + n) - 1
    p1 = m - 1
    p2 = n - 1

    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[i] = nums1[p1]
            i -= 1
            p1 -= 1
        else:
            nums1[i] = nums2[p2]
            i -= 1
            p2 -= 1

    return nums1


nums1 = [4, 5, 6, 0, 0, 0]
nums2 = [-4, -3, -1]


# print(merge(nums1, 3, nums2, 3))
# print(nums1 + nums2)


def sortedSquares(nums):
    res = collections.deque()
    l_pointer, r_pointer = 0, len(nums) - 1

    while l_pointer <= r_pointer:
        left, right = abs(nums[l_pointer]), abs(nums[r_pointer])
        if left > right:
            res.appendleft(pow(left, 2))
            l_pointer += 1
        else:
            res.appendleft(pow(right, 2))
            r_pointer -= 1
    return res


# print(sortedSquares(nums2))

def reverse_int(num):
    right = 0
    while num:
        left = num % 10
        right = right * 10 + left
        num = num // 10
    return right


def beautiful_day(i, j, k):
    res = 0
    for day in range(i, j + 1):
        if abs(day - reverse_int(day)) % k == 0:
            res += 1
    return res


print(beautiful_day(20, 23, 6))

