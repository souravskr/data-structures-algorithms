inputArr = [2, 3, 5, 6, 8, 13, 14, 20]


def binary_search(arr, target):
    left_arrow = arr[0]
    right_arrow = len(arr) - 1
    middle_point = int(len(arr) / 2)

    while(left_arrow <= right_arrow):
        if(arr[middle_point] == target):
            return target

        elif(target > arr[middle_point]):
            left_arrow = arr[middle_point + 1]
            print(left_arrow)

        elif(target < arr[middle_point]):
            right_arrow = arr[middle_point - 1]
        print(right_arrow)

        if(left_arrow > right_arrow):
            return -1


print(binary_search(inputArr, 13))
