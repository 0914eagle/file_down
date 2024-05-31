
def count_sequences(x, y):
    MOD = 10**9 + 7

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def power(a, b, mod):
        result = 1
        while b > 0:
            if b % 2 == 1:
                result = (result * a) % mod
            a = (a * a) % mod
            b //= 2
        return result

    if y % x != 0:
        return 0

    y //= x

    divisors = set()
    for i in range(1, int(y ** 0.5) + 1):
        if y % i == 0:
            divisors.add(i)
            divisors.add(y // i)

    ans = 0
    for d in divisors:
        count = power(2, d - 1, MOD)
        if count == d:
            ans = (ans + 1) % MOD

    return ans

x, y = map(int, input().split())
print(count_sequences(x, y))
