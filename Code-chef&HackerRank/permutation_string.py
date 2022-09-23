import collections


def check_inclusion(s1, s2):
    s_dict = string_to_dict(s1)
    s1_size = len(s1)
    size = len(s2) - s1_size
    matched = False

    for i in range(size+1):
        if s_dict == string_to_dict(s2[i:s1_size + i]):
            matched = True
    return matched


def string_to_dict(s):
    s_dict = {}
    i = 1
    for c in s:
        if c in s_dict:
            s_dict[c] += 1
        else:
            s_dict[c] = i
    return s_dict


s1 = "adc"
s2 = "dcda"
print(check_inclusion(s1, s2))