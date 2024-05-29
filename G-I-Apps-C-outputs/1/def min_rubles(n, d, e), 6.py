
def min_rubles(n, d, e):
    min_val = float('inf')

    for dollar in range(n // d + 1):
        for euro in range(n // e + 1):
            total_rubles = n - dollar * d - euro * e
            if total_rubles >= 0 and total_rubles < min_val:
                min_val = total_rubles

    return min_val

n = int(input())
d = int(input())
e = int(input())

print(min_rubles(n, d, e))
```
