def binary_search(arr, target):
    size = len(arr)
    left_pointer = 0
    right_pointer = size - 1

    while left_pointer <= right_pointer:
        mid = int((left_pointer + right_pointer) / 2)

        if target == arr[mid]:
            print(f'GIVEN LIST: {arr} \n TARGET: {target}')
            return f'FOUND! Index of {target} is {arr.index(target)}'
        elif target > mid:
            left_pointer = mid + 1
        else:
            right_pointer = mid - 1


my_list = [i for i in range(1, 11)]
target_input = 1
print(binary_search(arr=my_list, target=target_input))