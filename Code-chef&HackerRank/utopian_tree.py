def utopian_tree(n):
    res = 0
    for i in range(n + 1):
        if i % 2 == 0:
            res += 1
        else:
            res *= 2
    return res


print(utopian_tree(0))
