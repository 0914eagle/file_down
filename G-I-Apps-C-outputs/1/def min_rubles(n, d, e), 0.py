
def min_rubles(n, d, e):
    min_rubles = n % min(d, e)
    for i in range(n // min(d, e) + 1):
        rubles_left = n - i * min(d, e)
        rubles_left %= max(d, e)
        min_rubles = min(min_rubles, rubles_left)
    return min_rubles

# Read input
n = int(input())
d = int(input())
e = int(input())

# Output result
print(min_rubles(n, d, e))
```
