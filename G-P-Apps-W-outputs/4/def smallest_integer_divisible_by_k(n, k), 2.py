
def smallest_integer_divisible_by_k(n, k):
    x = n + (k - n % k)  # Find the next multiple of k greater than n
    return x

n, k = map(int, input().split())
print(smallest_integer_divisible_by_k(n, k))
```
