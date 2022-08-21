def even_fionacci_number(num):
    a, b = 1, 1
    res = 0
    while a <= num:
        if a % 2 == 0:
            res += a
        a, b = b, a + b
    return res

num = 4000000
print(even_fionacci_number(num))