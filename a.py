arr = [5, 6, 8, 16]


def insert_into(arr, num):
    arr = sorted(arr)
    arr.append(0)
    size = len(arr)
    for i in range(size):
        if num > arr[size - 2]:
            arr[size-1] = num
            return arr
        elif arr[i] > num:
            for j in range(size - 1, i, -1):
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
            arr[i] = num
            break

    return arr


print(insert_into(arr, 15))
