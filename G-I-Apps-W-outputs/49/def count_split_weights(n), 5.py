
def count_split_weights(n):
    weights = set()
    for i in range(1, n + 1):
        remaining = n
        count = 1
        while remaining >= i:
            weights.add(count)
            remaining -= i
            count += 1
    return len(weights)

n = int(input())
print(count_split_weights(n))
```
