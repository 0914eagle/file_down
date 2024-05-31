
def count_sequences(x, y):
    MOD = 10**9 + 7

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def count_factors(num):
        count = 0
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                count += 2 if num // i != i else 1
        return count

    if y % x != 0:
        return 0

    y //= x

    factors = count_factors(y)

    result = pow(2, factors - 1, MOD)
    return result

x, y = map(int, input().split())
print(count_sequences(x, y))
