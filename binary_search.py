arr = [5, 6, 8, 16]


def binary_search(arr, num):
    size = len(arr)
    l_pointer = 0
    r_pointer = size - 1

    while (l_pointer <= r_pointer):
        mid = int((l_pointer + r_pointer) / 2)

        if num == arr[mid]:
            return f"{num} in: {arr.index(num)} index"
        elif num < arr[mid]:
            r_pointer = mid - 1
        else:
            l_pointer = mid + 1

    return "Not Found!"


print(binary_search(arr, 8))
