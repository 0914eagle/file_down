
def exponial(n, m):
    if n == 1:
        return 1
    else:
        result = 1
        for i in range(n-1, 0, -1):
            result = pow(i, result, m)
        return result

# Input
n, m = map(int, input().split())

# Output
print(exponial(n, m))
```
