
def modp(n: int, p: int):
    result = 1
    base = 2

    if n == 0:
        return result

    n = n % (p - 1)
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        n = n // 2
        base = (base * base) % p

    return result

# Test cases
print(modp(3, 5))   # Output: 3
print(modp(1101, 101))   # Output: 2
print(modp(0, 101))   # Output: 1
print(modp(3, 11))   # Output: 8
print(modp(100, 101))   # Output: 1
