
def min_rubles_after_exchange(n, d, e):
    min_rubles = n
    for i in range(n//d + 1):
        rubles_left = n - i * d
        min_rubles = min(min_rubles, rubles_left % e)
    return min_rubles

n = int(input())
d = int(input())
e = int(input())

print(min_rubles_after_exchange(n, d, e))
```
