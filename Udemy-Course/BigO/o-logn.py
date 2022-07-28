def binary_search(my_list, target):
    size = len(my_list)
    left_pointer = 0
    right_pointer = size - 1

    while left_pointer <= right_pointer:
        mid_pointer = int((left_pointer + right_pointer) / 2)

        if my_list[mid_pointer] == target:
            print(f'GIVEN LIST: {my_list} \nTARGET: {target}')
            return f'{my_list.index(target)}'
        elif target > my_list[mid_pointer]:
            left_pointer = mid_pointer + 1
        else:
            right_pointer = mid_pointer - 1


my_list = [i for i in range(1, 11)]
target = 10
print(binary_search(my_list, target))