
def min_operations_to_make_equal(a, b):
    def num_operations(num, divisor, target):
        count = 0
        while num % divisor == 0 and num > target:
            num //= divisor
            count += 1
        return count

    operations = 0
    common_factors = 2, 3, 5
    for factor in common_factors:
        operations += num_operations(a, factor, b)
        operations += num_operations(b, factor, a)
    
    if a == b:
        return 0
    elif a % b == 0 or b % a == 0:
        return operations
    else:
        return -1

# Read input
a, b = map(int, input().split())

# Calculate and print result
result = min_operations_to_make_equal(a, b)
print(result)
```
