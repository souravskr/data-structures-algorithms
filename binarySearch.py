inputArr = [2, 3, 5, 6, 8, 13, 14, 20]


def binary_search(arr, target):
    left_arrow = 0
    right_arrow = len(arr) - 1

    while(left_arrow <= right_arrow):

        middle_point = int((left_arrow + right_arrow)/2)
        print(middle_point)
        if(arr[middle_point] == target):
            return target

        elif(target > arr[middle_point]):
            left_arrow = middle_point + 1
            # print(left_arrow)
        else:
            right_arrow = middle_point - 1
        # print(right_arrow, left_arrow)

    return -1


print(binary_search(inputArr, 13))
