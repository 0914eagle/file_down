
def min_operations_to_equal_numbers(n, k, a):
    min_element = min(a)
    operations = 0
    for num in a:
        diff = num - min_element
        operations += diff // 2
    return operations

# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Calculate and print the result
result = min_operations_to_equal_numbers(n, k, a)
print(result)
```
