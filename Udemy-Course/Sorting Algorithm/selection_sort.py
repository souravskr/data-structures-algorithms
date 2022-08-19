def selection_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        min_index = i
        for j in range(i + 1, size):
            if arr[min_index] > arr[j]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


my_arr = [4, 2, 6, 5, 1, 3]
print(selection_sort(my_arr))
