
def find_smallest_divisible(n, k):
    return n + (k - n % k)

n, k = map(int, input().split())
print(find_smallest_divisible(n, k))
```
