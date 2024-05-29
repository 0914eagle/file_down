
def min_operations(a, b):
    def try_divide(n, divisions):
        count = 0
        for div, weight in divisions:
            while n % div == 0:
                n //= div
                count += weight
        return count if n == 1 else -1

    divisions = [(2, 1), (3, 2), (5, 4)]
    operations_a = try_divide(a, divisions)
    operations_b = try_divide(b, divisions)

    if operations_a == -1 or operations_b == -1:
        return -1
    return abs(operations_a - operations_b)

a, b = map(int, input().split())
print(min_operations(a, b))
```
