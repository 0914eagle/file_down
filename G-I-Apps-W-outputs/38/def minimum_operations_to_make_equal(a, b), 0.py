
def minimum_operations_to_make_equal(a, b):
    def count_divisible_by(num, x):
        count = 0
        while num % x == 0:
            count += 1
            num //= x
        return count
    
    operations = 0
    for x in [2, 3, 5]:
        count_a = count_divisible_by(a, x)
        count_b = count_divisible_by(b, x)
        if (count_a - count_b) % 2 != 0:
            return -1
        operations += abs(count_a - count_b)
    
    return operations

a, b = map(int, input().split())
result = minimum_operations_to_make_equal(a, b)
print(result)
```
