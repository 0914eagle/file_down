
def smallest_integer_divisible(n, k):
    return n + (k - n % k)

# Taking input
n, k = map(int, input().split())

# Calling the function and printing the result
print(smallest_integer_divisible(n, k))
```
