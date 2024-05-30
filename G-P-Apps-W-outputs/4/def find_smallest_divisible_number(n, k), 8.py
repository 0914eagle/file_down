
def find_smallest_divisible_number(n, k):
    return n + (k - n % k) if n % k != 0 else n + k

# Input
n, k = map(int, input().split())

# Output
print(find_smallest_divisible_number(n, k))
```
