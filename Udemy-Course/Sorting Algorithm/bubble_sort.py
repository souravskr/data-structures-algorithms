import time


def bubble_sort(arr):
    size = len(arr)
    for i in range(size - 1, 1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
        time.sleep(1)
    return arr


my_arr = [4, 2, 6, 5, 1, 3]
print(bubble_sort(arr=my_arr))
