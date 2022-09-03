def fibo_series(num):
    res = []
    for i in range(num + 1):
        if i == 0 or i == 1:
            res.append(1)
        else:
            next_item = res[-1] + res[-2]
            res.append(next_item)
    return res


def fibo_recursive(num):
    if num <= 1:
        return 1
    return fibo_recursive(num - 1) + fibo_recursive(num - 2)


print(fibo_series(6))

print(fibo_recursive(6))