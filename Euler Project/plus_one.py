def plus_one(arr):
    # if 0 not in arr:
    #     arr[-1] += 1
    #     n = arr[-1]
    #     while n:
    #         l = n % 10
    #         arr.append(l)
    #         n = n // 10
    #     arr.pop(-3)
    #     arr[-2], arr[-1] = arr[-1], arr[-2]
    arr_string = [str(i) for i in arr]
    arr_string = int(''.join(arr_string))
    arr_string += 1
    res = []
    while arr_string:
        right = arr_string % 10
        res.append(right)
        arr_string = arr_string // 10
    res.reverse()
    return res


digits = [9]
print(plus_one(digits))
