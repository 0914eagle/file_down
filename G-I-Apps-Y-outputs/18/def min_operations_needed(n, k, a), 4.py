
def min_operations_needed(n, k, a):
    a.sort()
    unique_a = list(set(a))
    
    min_operations = float('inf')
    
    for num in unique_a:
        count = a.count(num)
        operations = 0
        while count < k:
            num //= 2
            operations += 1
            count *= 2
        min_operations = min(min_operations, operations)
    
    return min_operations

# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Call the function and output the result
print(min_operations_needed(n, k, a))
```
