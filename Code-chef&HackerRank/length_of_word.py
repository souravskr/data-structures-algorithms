import collections

word = "leet1234code234"


def my_fn(word):
    size = len(word)
    end = size - 1
    num = ''
    for i in range(size):
        if word[i].isdigit():
            num += word[i]
            if i == end:
                num += ' '

        else:
            num += ' '
    res_lst = collections.Counter([int(x) for x in num.split()])
    return len(res_lst)


print(my_fn(word))
