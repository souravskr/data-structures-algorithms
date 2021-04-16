arr = [8, 5, 6, 16]


def insert_into(arr, num):
    arr = sorted(arr)
    size = len(arr)
    i = 0
    while (i < size):
        if arr[i] > num:
