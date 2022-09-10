def angry_professor(k, a):
    on_time = 0
    for i in a:
        if i <= 0:
            on_time += 1
    print(on_time)
    if on_time >= k:
        return 'YES'
    return 'NO'


arr = [-1, -3, 4, 2]
k = 3
print(angry_professor(k, arr))
