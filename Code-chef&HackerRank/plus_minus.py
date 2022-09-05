def plus_minus(arr):
    count_positive = 0
    count_negative = 0
    count_zeros = 0

    for i in arr:
        if i == 0:
            count_zeros += 1
        elif i < 0:
            count_negative += 1
        else:
            count_positive += 1

    size = len(arr)
    positive_portions = format(count_positive/size, '.6f')
    negative_portions = format(count_negative/size, '.6f')
    zero_portions = format(count_zeros/size, '.6f')

    print(positive_portions)
    print(negative_portions)
    print(zero_portions)


arr = [-4, 3, -9, 0, 4, 1]
plus_minus(arr)

