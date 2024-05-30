
def infinite_tetration(N):
    def f(a):
        return a ** f(a - 1) if a > 0 else 1

    epsilon = 1e-5
    low, high = 0, 10
    while True:
        mid = (low + high) / 2
        if f(mid) > N:
            high = mid
        else:
            low = mid
        if abs(f(mid) - N) < epsilon:
            return mid

N = float(input())
result = infinite_tetration(N)
print("{:.6f}".format(result))
```
