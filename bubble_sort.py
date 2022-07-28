arr = [3, 1, 2, 5, 4, 11, 8, 7, 9, 10]


def bubble_sort(arr):
    size = len(arr) - 1
    sorted = False
    while (not sorted):
        sorted = True
        for i in range(size):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
        size -= 1
    return arr
sorted_arr = bubble_sort(arr)

print(sorted_arr)
