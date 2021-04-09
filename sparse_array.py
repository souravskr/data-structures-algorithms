arr = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 'sdaklfj',
       'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf']
qur = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn']


# def matchingStrings(arr, qur):
#     output_dict = {}
#     for i in qur:
#         k = 1
#         for j in arr:
#             if i == j:
#                 output_dict[i] = k
#                 k += 1
#             if output_dict.get(i):
#                 continue
#             output_dict[i] = 0

#     output = [*output_dict.values()]
#     return output

def arr_to_dict(arr):
    arr_dict = {}
    for i in arr:
        if arr_dict.get(i):
            arr_dict[i] += 1
        else:
            arr_dict[i] = 1
    return arr_dict


def matchingStrings(strings, queries):
    str_dict = arr_to_dict(strings)
    output = []
    for i in queries:
        if str_dict.get(i):
            output.append(str_dict.get(i))
        else:
            output.append(0)

    return output


print(matchingStrings(arr, qur))
