arr = [0, 1, 2]
# arr = [1, 2, 3, 4, 5]
d = 4


# def right_rotate(arr, d):
#     size = len(arr)
#     c_arr = [0] * (size)

#     j = 2
#     for _ in range(d):
#         for i in range(1):
#             c_arr[0] = arr[j]
#             c_arr[i+1] = arr[i]
#             c_arr[i+2] = arr[i+1]
#         print(c_arr)
#         arr = c_arr
#         c_arr = [0] * (size)

#     return arr

def right_rotate(arr, d):
    size = len(arr)
    print(f"Input: {arr}")
    c_arr = [0] * (size)

    k = size - 1
    for _ in range(d):
        for i in range(1):
            c_arr[0] = arr[k]
            for i in range(k):
                c_arr[i+1] = arr[i]
            # c_arr[i+2] = arr[i+1]
        print(f"Rotate-{_+1}: {c_arr}")
        arr = c_arr
        c_arr = [0] * (size)

    return arr


(right_rotate(arr, d))
# print(right_rotate(arr, d))
