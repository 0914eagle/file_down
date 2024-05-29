
def min_rubles(n, d, e):
    min_rubles = float('inf')
    for num_dollars in range(n // d + 1):
        for num_euros in range(n // e + 1):
            total_rubles = n - num_dollars * d - num_euros * e * 5
            if total_rubles >= 0 and total_rubles < min_rubles:
                min_rubles = total_rubles
    return min_rubles

n = int(input())
d = int(input())
e = int(input())

print(min_rubles(n, d, e))
```
