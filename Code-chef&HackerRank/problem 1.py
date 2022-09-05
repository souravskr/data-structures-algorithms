def fibo_series(num):
    res = []
    for i in range(num + 1):
        if i == 0 or i == 1:
            res.append(1)
        else:
            next_item = res[-1] + res[-2]
            res.append(next_item)
    return res[-1]


def fibo_recursive(num):
    if num <= 1:
        return 1
    return fibo_recursive(num - 1) + fibo_recursive(num - 2)


print(fibo_series(45))


# print(fibo_recursive(50))


def find_first_n_last(arr, target):
    if target not in arr:
        return [-1, -1]
    arr.sort()
    target_count = arr.count(target)
    print(target_count)
    start_index = arr.index(target)
    last_index = start_index + target_count - 1
    return [i for i in range(start_index, last_index + 1)]


new_array = [75, 99, 19, 93, 87, 68, 12, 18, 48, 83, 24, 50, 16, 53, 36, 16, 80, 68, 46, 13, 53, 100, 50, 49, 77, 52,
             34, 42, 38, 98, 73, 11, 13, 61, 72, 8, 11, 67, 98, 24, 23, 71, 47, 6, 5, 7, 97, 86, 25, 82, 11, 15, 26, 97,
             69, 6, 30, 77, 98, 44, 32, 39, 71, 47, 64, 78, 6, 61, 72, 75]

print(find_first_n_last(new_array, 98))

arr = [[2, 3]]

c = arr.pop()
print(*c)