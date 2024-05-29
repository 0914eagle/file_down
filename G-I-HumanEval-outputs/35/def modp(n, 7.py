
def modp(n: int, p: int):
    if p == 1:
        return 0
    result = 1
    power_of_2 = 2 % p
    while n > 0:
        if n % 2 == 1:
            result = (result * power_of_2) % p
        n = n >> 1
        power_of_2 = (power_of_2 * power_of_2) % p
    return result

# Testing the function
print(modp(3, 5))  # Output should be 3
print(modp(1101, 101))  # Output should be 2
print(modp(0, 101))  # Output should be 1
print(modp(3, 11))  # Output should be 8
print(modp(100, 101))  # Output should be 1
