arr = [0, 1, 2]
d = 4


def right_rotate(arr, d):
    size = len(arr)
    c_arr = [0] * size

    i = 0
    rotate_index = d + 1
    while (rotate_index < size):
        c_arr[i] = arr[rotate_index]
        i += 1
        rotate_index += 1
    print(c_arr)
    rotate_index = 0
    while (rotate_index <= d):
        c_arr[i] = arr[rotate_index]
        i += 1
        rotate_index += 1

    return c_arr


print(right_rotate(arr, d))
