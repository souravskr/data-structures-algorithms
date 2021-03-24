inputArr = [2, 3, 5, 6, 8, 13, 14, 20]


def binary_search(arr, target):

    left_pointer = 0
    right_pointer = len(arr) - 1

    while(left_pointer <= right_pointer):

        mid_pointer = int((left_pointer + right_pointer)/2)

        if (target == arr[mid_pointer]):
            return mid_pointer

        elif (target > arr[mid_pointer]):
            left_pointer = mid_pointer + 1

        else:
            right_pointer = mid_pointer - 1

    return -1


print(binary_search(inputArr, 13))
