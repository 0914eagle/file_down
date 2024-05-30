
def find_smallest_divisible(n, k):
    x = n + k - n % k
    return x

# Input
n, k = map(int, input().split())

# Output
print(find_smallest_divisible(n, k))
```
