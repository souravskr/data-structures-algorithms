def firstRecurringChar(arr):
    map_dict = {}
    for i in range(len(arr)):
        if arr[i] in map_dict:
            return arr[i]
        map_dict[arr[i]] = i

    return None


arr = [2, 2, 3, 4, 5, 5]

print(firstRecurringChar(arr))
