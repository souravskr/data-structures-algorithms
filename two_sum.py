numbers = [3, 2, 4]
target = 6
copy_numbers = numbers.copy()
numbers.sort()

left_pointer = 0
right_pointer = len(numbers) - 1

output = []

for i in range(len(numbers)):
    two_sum = numbers[left_pointer] + numbers[right_pointer]

    if two_sum > target:
        right_pointer -= 1
    elif two_sum < target:
        left_pointer += 1

    if numbers[left_pointer] == numbers[right_pointer]:
        output.append(copy_numbers.index(numbers[left_pointer], copy_numbers.index(numbers[left_pointer],
                                                                                   left_pointer + 1)))
        break

    output.append(copy_numbers.index(numbers[left_pointer], copy_numbers.index(numbers[left_pointer],
                                                                               left_pointer + 1)))
    break

print(output)
