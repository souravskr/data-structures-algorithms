def bubble_sort(arr):
    size = len(arr)
    for i in range(size, 0, -1):
        for j in range(size - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


my_list = [4, 3, 2, 1]
print(bubble_sort(my_list))


def remove_duplicates(arr):
    size = len(arr)
    left = 1
    right = 1
    for i in range(1, size):
        if arr[right] == arr[right - 1]:
            right += 1
        else:
            arr[left] = arr[right]
            left += 1
            right += 1
    return arr


dup = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# dup = [1, 1, 2]
print(remove_duplicates(dup))


def selection_sort(arr):
    size = len(arr)

    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


my_list = [4, 3, 2, 1]
print(selection_sort(my_list))


def max_value(arr):
    # Some sort of bubble sort
    size = len(arr)
    for i in range(size - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr[-1]


my_list = [4, 3, 2, 1, 9]
print(max_value(my_list))
