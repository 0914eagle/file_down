
def min_operations(a, b):
    def prime_factors(n):
        factors = []
        d = 2
        while d*d <= n:
            while (n % d) == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors

    a_factors = set(prime_factors(a))
    b_factors = set(prime_factors(b))

    if a_factors != b_factors:
        return -1

    diff_ops = []
    for factor in a_factors:
        count_a = 0
        count_b = 0
        while a % factor == 0:
            a //= factor
            count_a += 1
        while b % factor == 0:
            b //= factor
            count_b += 1
        diff_ops.append(abs(count_a - count_b))

    return sum(diff_ops)

a, b = map(int, input().split())
result = min_operations(a, b)
print(result)
```
