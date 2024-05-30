
import math

def find_infinite_tetration_N(N):
    def f(a):
        return a**f(a-1) if a > 0 else 1

    def solve(a, N):
        return f(a) - N

    a = N
    while solve(a, N) > 1e-5:
        a = math.log(N) / math.log(f(a))
    return a

N = float(input())
result = find_infinite_tetration_N(N)
print(f"{result:.6f}")
```
