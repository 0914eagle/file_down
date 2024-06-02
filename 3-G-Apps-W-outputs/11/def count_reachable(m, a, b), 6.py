
def count_reachable(m, a, b):
    if a == 1 or b == 1:
        return m + 1

    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    ab_gcd = gcd(a, b)
    period = a + b - ab_gcd

    def f(x):
        if x < a:
            return x + 1
        if x < b:
            return a
        if x < period:
            return a + 1
        return a + 2

    full_periods = m // period
    remainder = m % period

    return full_periods * (f(period) - f(0)) + f(remainder)

m, a, b = map(int, input().split())
print(sum(count_reachable(i, a, b) for i in range(m + 1)))
