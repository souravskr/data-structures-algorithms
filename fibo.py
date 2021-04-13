# def fibo(n):
#     if n == 1 or n == 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n - 2)


# print(fibo(10))

original_ist = ['one', 'two', 'three', 'four']
add_ist = ['one', 'two', 'five', 'six']
delete_list = ['two', 'five']


output = {}
for i in original_ist+add_ist:
    output[i] = len(i)

for i in delete_list:
    output.pop(i)

dict_out = output.copy()

# keys = list(output.keys())
# values = list(output.values())
# a = sorted(output.items(), key=lambda x: x[1], reverse=True)


out_arr = []

for _ in range(len(output)):
    max_key = max(output, key=output.get)
    out_arr.append(max_key)
    output.pop(max_key)

# print(out_arr)

d = {}

for key, value in dict_out.items():
    if value not in d:
        d[value] = [key]
    else:
        d[value].append(key)

print(sorted(d, reverse=True))

# for value in d.values():
#     print(sorted(value, reverse=True))

# a = sorted(d.items(), reverse=True)
# print(a)
# resu = []
# for i in a:
