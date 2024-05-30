
def find_smallest_divisible_number(n, k):
    x = n + (k - n % k)
    return x

n, k = map(int, input().split())
result = find_smallest_divisible_number(n, k)
print(result)
```
