# def quick_sort(arr):
#     size = len(arr)
#     first = arr[0]
#
#     for i in range(1, size):
#
#         if first < arr[i]:
#             c = i
#         else:
#             if i == 1:
#                 continue
#             else:
#                 arr[c], arr[i] = arr[i], arr[c]
#                 c += 1
#     arr[0], arr[c-1] = arr[c -1], arr[0]
#     return arr


def quick_sort(arr, left, right):
    if left < right:
        pivot_index = pivot(arr, left, right)
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)
    return arr


def pivot(arr, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
    arr[pivot_index], arr[swap_index] = arr[swap_index], arr[pivot_index]
    return swap_index


my_list = [4, 2, 7, 1, 3]
# print(pivot(my_list, 0, 4))
# print(my_list)
print(quick_sort(my_list, 0, 4))
