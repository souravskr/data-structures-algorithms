#  Need to loop only half of the array and swap

def reverseArray(arr):
    size = len(arr)
    if size > 1:
        lastIndex = size - 1
        iterations = int(size / 2)

        for i in range(0, iterations):
            temp = arr[i]
            arr[i] = arr[lastIndex]
            arr[lastIndex] = temp
            lastIndex -= 1

        return arr
    return arr


print(reverseArray([1, 4, 3, 2]))
