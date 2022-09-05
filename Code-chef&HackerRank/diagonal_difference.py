def diagonal_difference(arr):
    first_diag = 0
    second_diag = 0
    size = len(arr)
    j = size - 1
    for i in range(size):
        first_diag += arr[i][i]
        second_diag += arr[i][j]
        j -= 1

    return abs(first_diag - second_diag)


two_d_array = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

print(diagonal_difference(two_d_array))
