arr = [1, 2, 3, 4, 5]
d = 2


def left_rotation(arr, d):
    size = len(arr)
    c_arr = [0] * size

    i = 0
    rotated_index = d

    while(rotated_index < size):
        c_arr[i] = arr[rotated_index]
        i += 1
        rotated_index += 1

    rotated_index = 0

    while(rotated_index < d):
        c_arr[i] = arr[rotated_index]
        i += 1
        rotated_index += 1

    return c_arr


print(left_rotation(arr, d))


# arr = arr[d:] + arr[:d]

# print(*arr)
