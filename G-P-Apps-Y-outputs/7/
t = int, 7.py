
t = int(input())
for _ in range(t):
    n = int(input())
    x = 1
    while n % x != 0:
        x *= 2
    print(n // x)
```
