def compare_triplets(a, b):
    score_a = 0
    score_b = 0
    for i in range(3):
        if a[i] > b[i]:
            score_a += 1
        elif b[i] > a[i]:
            score_b += 1
        else:
            continue
    return [score_a, score_b]


a = [17, 28, 30]
b = [99, 16, 8]
print(compare_triplets(a, b))

print(sum(a))