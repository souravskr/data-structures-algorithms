from binary_search import binary_search
arr = [4, 6, 10, 12, 16]


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


# insert with binary search

def insert_with_binary_search(arr, num):
    position = binary_search(arr, num)
    # print("position: ", position)
    arr.append(0)
    size = len(arr)
    if num < arr[position]:
        for j in range(size - 1, position, -1):
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
        arr[position] = num
    else:
        for j in range(size - 1, position+1, -1):
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            # print(j)

        arr[position+1] = num

    return arr


print(insert_with_binary_search(arr, 3))


def step_counter(num):
    count = 0
    while num > 1:
        num = int(num/2)
        count += 1
    return count


print(step_counter(100000))
