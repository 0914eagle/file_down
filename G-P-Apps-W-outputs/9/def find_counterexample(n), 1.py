
def find_counterexample(n):
    for m in range(1, 1001):
        if (n * m) + 1 not in [2, 3] and all((n * m) + 1 % i != 0 for i in range(2, int(((n * m) + 1) ** 0.5) + 1)):
            return m

n = int(input())
print(find_counterexample(n))
```
