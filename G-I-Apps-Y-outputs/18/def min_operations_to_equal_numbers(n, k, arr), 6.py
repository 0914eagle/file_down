
def min_operations_to_equal_numbers(n, k, arr):
    min_num = min(arr)
    operations = 0
    for num in arr:
        diff = max(0, num - (min_num * k))
        # Calculate the number of operations needed to make current number equal to min_num * k
        operations += len(bin(diff)) - 3
    return operations

# Read input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Call the function and print the result
print(min_operations_to_equal_numbers(n, k, arr))
```
