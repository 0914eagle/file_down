
def min_remaining_rubles(n, d, e):
    min_rubles = n
    for i in range(n // d + 1):
        rubles_left = n - i * d
        euros = rubles_left // e
        rubles_left %= e
        min_rubles = min(min_rubles, rubles_left)
    return min_rubles

n = int(input())
d = int(input())
e = int(input())

print(min_remaining_rubles(n, d, e))
```
