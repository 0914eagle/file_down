
def standing_spectators(n, k, t):
    if t <= k:
        return t
    elif t <= n:
        return k
    else:
        return n + k - t

# Input processing
n, k, t = map(int, input().split())

# Call the function and print the result
print(standing_spectators(n, k, t))
```
