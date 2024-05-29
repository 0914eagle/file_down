
def count_weights(n):
    weights = set()
    for i in range(1, n + 1):
        remaining_sum = n
        j = i
        while remaining_sum >= j:
            weights.add(remaining_sum)
            remaining_sum -= j
            j += 1
    return len(weights)

n = int(input())
result = count_weights(n)
print(result)
```
