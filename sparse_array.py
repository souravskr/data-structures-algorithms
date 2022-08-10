def arr_to_dict(arr):
    arr_dict = {}
    for i in arr:
        if arr_dict.get(i):
            arr_dict[i] += 1
        else:
            arr_dict[i] = 1
    return arr_dict


def matching_strings(strings, queries):
    str_dict = arr_to_dict(strings)
    output = []
    for i in queries:
        if str_dict.get(i):
            output.append(str_dict.get(i))
        else:
            output.append(0)

    return output


my_list = ['abcde', 'sdaklfj', 'asd', 'na', 'basdn', 'sdaklfj',
           'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf']
qur_list = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn']

print(matching_strings(my_list, qur_list))
