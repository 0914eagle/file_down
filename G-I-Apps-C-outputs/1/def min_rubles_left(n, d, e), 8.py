
def min_rubles_left(n, d, e):
    min_rubles = n
    for i in range(n//d + 1):
        for j in range(n//e + 1):
            current_rubles = n - (i*d + j*e)
            if current_rubles < min_rubles and current_rubles >= 0:
                min_rubles = current_rubles
    return min_rubles

n = int(input())
d = int(input())
e = int(input())
print(min_rubles_left(n, d, e))
```
