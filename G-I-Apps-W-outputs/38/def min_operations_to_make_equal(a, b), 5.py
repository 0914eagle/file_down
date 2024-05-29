
def min_operations_to_make_equal(a, b):
    def min_prime_factors(n):
        factors = []
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    a_factors = min_prime_factors(a)
    b_factors = min_prime_factors(b)

    if sorted(a_factors) != sorted(b_factors):
        return -1

    a_ops = sum([1 for factor in a_factors if factor not in [2, 3, 5]])
    b_ops = sum([1 for factor in b_factors if factor not in [2, 3, 5]])

    return abs(a_ops - b_ops)

# Input
a, b = map(int, input().split())

# Output
print(min_operations_to_make_equal(a, b))
```
