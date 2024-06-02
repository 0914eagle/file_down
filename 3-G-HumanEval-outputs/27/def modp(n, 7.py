
def modp(n: int, p: int):
    result = 1
    base = 2 % p
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        n //= 2
    return result

# Test cases
print(modp(3, 5))    # Output: 3
print(modp(1101, 101))    # Output: 2
print(modp(0, 101))    # Output: 1
print(modp(3, 11))    # Output: 8
print(modp(100, 101))    # Output: 1
