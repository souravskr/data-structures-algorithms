for i in range(1, 11):
    for j in range(1, 11):
        if j == 10:
            int_number = int(f'{i}{j-1}')
            print(int_number + 1)
        else:
            print(f'{i}{j}')

