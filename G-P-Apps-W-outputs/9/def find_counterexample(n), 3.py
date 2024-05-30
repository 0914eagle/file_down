
def find_counterexample(n):
    for m in range(1, 1001):
        if (n * m + 1) % 2 == 0:
            return m

n = int(input())
print(find_counterexample(n))
```
