from math import sqrt


def largest_prime_factors(num):
    i = 2
    while i * i < num:
        if num % i:
            i += 1
        else:
            num = int(num / i)
    return num


print(largest_prime_factors(600851475143))


# def is_prime(n):
#     for i in range(2, int(n / 2) + 1):
#         if (n % i) == 0:
#             return False
#     return True


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


def get_prime_factors(num):
    prime_factors = []
    for i in range(2, num + 1):
        if is_prime(i) and num % i == 0:
            prime_factors.append(i)
    return prime_factors


print(get_prime_factors(600851475143))

print(is_prime(4))
