def merge_sort(arr):
    size = len(arr)
    if size == 1:
        return arr
    mid = int(size/2)
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(arr1, arr2):
    i = 0
    j = 0
    combined = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            combined.append(arr1[i])
            i += 1
        else:
            combined.append(arr2[j])
            j += 1
    while i < len(arr1):
        combined.append(arr1[i])
        i += 1
    while j < len(arr2):
        combined.append(arr2[j])
        j += 1

    return combined


l1 = [2, 5, 8]
l2 = [3, 6, 7]
print(merge(l1, l2))
