
def min_rubles_left(n, d, e):
    min_rubles = n
    for i in range(n // d + 1):
        rubles_left = n - i * d
        rubles_left_after_euro = rubles_left % e
        min_rubles = min(min_rubles, rubles_left_after_euro)
    return min_rubles

n = int(input())
d = int(input())
e = int(input())

result = min_rubles_left(n, d, e)
print(result)
```
