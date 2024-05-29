
def min_rubles(n, d, e):
    min_rubles = n
    for i in range(n // d, -1, -1):
        remaining_rubles = n - i * d
        num_euro = remaining_rubles // e
        remaining_rubles -= num_euro * e
        min_rubles = min(min_rubles, remaining_rubles)
    return min_rubles

n = int(input())
d = int(input())
e = int(input())

print(min_rubles(n, d, e))
```
