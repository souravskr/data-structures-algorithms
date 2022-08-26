def is_power_of_three(n):
    if n == 1:
        return True
    if n == 0 or n % 3 != 0:
        return False
    n = n / 3
    return is_power_of_three(n)


print(is_power_of_three(81))
