
def count_weights(n):
    weights = set()
    for i in range(1, n+1):
        if n % i == 0:
            weights.add(n // i)
    return len(weights)

n = int(input())
print(count_weights(n))
```
