import time


def insertion_sort(arr):
    size = len(arr)
    for i in range(1, size):
        temp = arr[i]
        position = i - 1
        while position >= 0 and arr[position] > temp:
            arr[position + 1] = arr[position]
            arr[position] = temp
            position -= 1
    return arr


my_arr = [4, 2, 7, 1, 3]
print(insertion_sort(my_arr))
 