def mini_max_sum(arr):
    i = 0
    res_arr = []
    size = len(arr)
    while i < size:
        new_arr = arr.copy()
        new_arr.pop(i)
        res_arr.append(sum(new_arr))
        i += 1
    print(f'{min(res_arr)} {max(res_arr)}')


arr = [1, 2, 3, 4, 5]

mini_max_sum(arr)
