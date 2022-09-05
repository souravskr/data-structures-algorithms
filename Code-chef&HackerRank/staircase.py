def staircase(n):
    space = ' '
    symbol = '#'
    j = n - 1
    for i in range(1, n + 1):
        print(j * space + i * symbol)
        j -= 1


staircase(6)
