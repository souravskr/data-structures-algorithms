
a = [8, 5, 6, 16, 5]
l = 1
r = 3

size = len(a)
b = []

for i in range(size):
    x1 = a[i] % (i + 1)
    if x1 == 0:
        x = a[i] // (i + 1)
        if a[i] == (i + 1) * x:
            if x >= l and x <= r:
                b.append(True)
            else:
                b.append(False)

    else:
        b.append(False)


print(b)
