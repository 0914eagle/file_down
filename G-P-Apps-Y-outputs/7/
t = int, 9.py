
t = int(input())

for _ in range(t):
    n = int(input())
    x = 1
    while n % (2*x - 1) != 0:
        x *= 2
    print(n // (2*x - 1))
```
