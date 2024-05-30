
def exponial(n, m):
    result = 1
    for i in range(n, 0, -1):
        result = pow(i, result, m)
    return result

n, m = map(int, input().split())
print(exponial(n, m))
```
