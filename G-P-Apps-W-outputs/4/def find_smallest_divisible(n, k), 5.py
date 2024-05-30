
def find_smallest_divisible(n, k):
    x = n // k * k + k
    return x

# Read input
n, k = map(int, input().split())

# Call function and print the result
print(find_smallest_divisible(n, k))
```
