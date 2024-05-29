
def count_weights_of_splits(n):
    counts = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            counts.add(i)
            counts.add(n // i)
    return len(counts)

n = int(input())
print(count_weights_of_splits(n))
```
