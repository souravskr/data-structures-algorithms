# Call Stack

def three():
    print('Three')


def two():
    three()
    print('Two')


def one():
    two()
    print('One')


one()


# Factorial

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(4))
