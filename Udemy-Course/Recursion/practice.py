# YouTube Lecture by Alvin
import time


# Base Case: the smallest instance of a problem that is solved trivially
# Recursive Case: an instance of a problem that shrinks the size of the input toward the base case.

# Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


# print(factorial(5))


# Sum of All Elements
def sum_elements(nums):
    size = len(nums)
    if not size:
        return 0
    num = nums.pop(0)
    return num + sum_elements(nums)


# print(sum_elements([1, 5, 7, -2]))


# another solution
def sum_array(nums):
    size = len(nums)
    if not size:
        return 0
    print(nums)
    num = nums.pop(size - 1)
    time.sleep(2)
    return num + sum_array(nums)


# print(sum_array([1, 5, 7, -2]))


def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(5))


def check_powers_of_three(n):
    res = 0
    i = 0
    while res <= n:
        if res == n:
            return True
        res = res + (3 ** i)
        i += 1
    return False


# print(check_powers_of_three(91))

