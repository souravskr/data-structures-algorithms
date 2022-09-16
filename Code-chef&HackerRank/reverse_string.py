# def reverseWords(s):
#     s = s.split()
#     return " ".join(str(item[::-1]) for item in s)
#     # res = ''
#     # for w in s:
#     #     res += w[::-1] + ' '
#     # return res
#
#
# print(reverseWords("Let's take LeetCode contest"))

def find_original_array(changed):
    size = len(changed)
    if size % 2 != 0:
        return []

    # mid = int(size / 2)
    # first_half = changed[:mid]
    # last_half = changed[mid:]
    # if [i*2 for i in first_half] == last_half:
    #     return first_half
    # elif [i*2 for i in last_half] == first_half:
    #     return last_half
    # size = len(changed)
    mid = int(size / 2)
    # if size % 2 != 0:
    #     return []
    # res = []
    # for i in changed:
    #     if i * 2 in changed:
    #         res.append(i)
    #         if len(res) == mid:
    #             return res
    # return []
    # res = []
    # c_changed = []
    # for i in range(size):
    #     if changed[i] % 2 == 0:
    #         res.append(changed[i])
    #     else:
    #         c_changed.append(changed[i])
    #
    # if [i * 2 for i in c_changed] == res:
    #     return c_changed
    # return []
    # res = []
    # for i in changed:
    #     if len(res) >= mid:
    #         break
    #     elif i == 0 and changed.count(i) > 2:
    #         res.append(i)
    #     elif len(res) < mid and i != 0 and changed.count(i * 2) >= 1:
    #         res.append(i)
    #
    # if len(res) == mid:
    #     return res
    # return []

    original = []

    for left in range(size):
        right = size - 1
        while left < right and len(original) < mid:
            if changed[left] * 2 == changed[right]:
                original.append(changed[left])
            elif changed[right] * 2 == changed[left]:
                original.append(changed[right])
            right -= 1

    if len(original) == mid:
        return original
    return []

    # while left < right and len(original) <= mid:
    #     if changed[right] * 2 == changed[left]:
    #         original.append(changed[right])
    #     left += 1
    #     right -= 1




changed = [0, 0, 0, 0]
print(find_original_array(changed))
