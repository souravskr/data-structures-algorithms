a = [[3, 3, 4, 2],
     [4, 4],
     [4, 0, 3, 3],
     [2, 3],
     [3, 3, 3]]


def meanGroups(a):
    b = []
    j = 0
    for i in a:
        a[j] = (sum(i)/len(i))
        j += 1

    output = {}

    for i in range(len(a)):
        if output.get(a[i]):
            output[a[i]].append(i)
        else:
            output[a[i]] = [i]

    j = 0
    for item in output.values():
        b.append(item)
        j += 1
    return b


print(meanGroups(a))
