inputArr = [4, 5, 6, 7, 0, 1, 2, 3]


def shifted_binary_search(input_arr, target):
    min_value = min(input_arr)
    max_value = max(input_arr)
    last_elem = input_arr[len(input_arr) - 1]

    if target <= last_elem:
        left_pointer = input_arr.index(min_value)
        right_pointer = len(input_arr) - 1

        while left_pointer <= right_pointer:
            mid_pointer = int((left_pointer + right_pointer)/2)
            if target == input_arr[mid_pointer]:
                return mid_pointer
            elif target > input_arr[mid_pointer]:
                left_pointer = mid_pointer + 1
            else:
                right_pointer = mid_pointer - 1

    else:
        left_pointer = 0
        right_pointer = input_arr.index(max_value)
        while left_pointer <= right_pointer:
            mid_pointer = ((left_pointer + right_pointer)//2)
            if target == input_arr[mid_pointer]:
                return mid_pointer
            elif target > input_arr[mid_pointer]:
                left_pointer = mid_pointer + 1
            else:
                right_pointer = mid_pointer - 1

    return -1


print(shifted_binary_search(inputArr, 7))
