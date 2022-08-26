def combinations(arr):
    size = len(arr)
    if not size:
        return [[]]
    first_element = arr[0]
    rest = arr[1:]
    combs_without_first = combinations(rest)
    combs_with_first = [[first_element] + char for char in combs_without_first]
    return combs_without_first + combs_with_first


an_arr = [i for i in range(1, 5)]
print(combinations(an_arr))
