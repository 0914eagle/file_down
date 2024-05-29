
def calculate_operations(a, b):
    def get_factors(n):
        factors = []
        factor = 2
        while factor * factor <= n:
            if n % factor:
                factor += 1
            else:
                n //= factor
                factors.append(factor)
        if n > 1:
            factors.append(n)
        return factors

    a_factors = get_factors(a)
    b_factors = get_factors(b)

    a_factors_set = set(a_factors)
    b_factors_set = set(b_factors)

    if a_factors_set != b_factors_set:
        return -1

    common_factors = a_factors_set.intersection(b_factors_set)

    combined_operations = 0
    for factor in common_factors:
        a_factor_count = a_factors.count(factor)
        b_factor_count = b_factors.count(factor)
        combined_operations += abs(a_factor_count - b_factor_count)

    return combined_operations

# Parsing input
a, b = map(int, input().split())

# Calculate and print the minimum number of operations
print(calculate_operations(a, b))
```
