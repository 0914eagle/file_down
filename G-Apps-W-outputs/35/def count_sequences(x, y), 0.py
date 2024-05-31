
def count_sequences(x, y):
    mod = 10**9 + 7

    # Function to calculate modular inverse
    def mod_inverse(a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    # Function to calculate power under mod
    def power_mod(a, b, m):
        result = 1
        a = a % m
        while b > 0:
            if b % 2 == 1:
                result = (result * a) % m
            b = b // 2
            a = (a * a) % m
        return result

    # Function to calculate number of divisors of x
    def num_divisors(x):
        divisors = 0
        i = 1
        while i * i <= x:
            if x % i == 0:
                if x // i == i:
                    divisors += 1
                else:
                    divisors += 2
            i += 1
        return divisors

    if y % x != 0:
        return 0

    num_factors = num_divisors(x)
    return power_mod(num_factors, y // x - 1, mod) % mod

# Input
x, y = map(int, input().split())
# Output
print(count_sequences(x, y))
