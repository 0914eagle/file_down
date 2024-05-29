
def count_weights(n):
    if n == 1:
        return 1
    weights = set()
    for i in range(1, int(n**0.5) + 1):
        remainder = n % i
        if remainder == 0:
            weights.add(i)
            weights.add(n // i)
    return len(weights)

n = int(input())
result = count_weights(n)
print(result)
```
