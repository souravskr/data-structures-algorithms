# Print Numbers without loop

def print_numbers(start):
    if start > 100:
        return "The End!"

    print(start)
    print_numbers(start + 1)


print(print_numbers(1))
