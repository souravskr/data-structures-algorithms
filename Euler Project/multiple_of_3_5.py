def multiple_of_3_5(num):
    res = 0
    for i in range(1, num):
        if i % 3 ==0 or i % 5 == 0:
            # print(i)
            res += i
    return res


print(multiple_of_3_5(1000))
