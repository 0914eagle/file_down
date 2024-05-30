
def find_smallest_integer(n, k):
    if n % k == 0:
        return n + k
    else:
        return n + (k - n % k)

# Reading input
n, k = map(int, input().split())

# Calling the function and printing the result
print(find_smallest_integer(n, k))
```
