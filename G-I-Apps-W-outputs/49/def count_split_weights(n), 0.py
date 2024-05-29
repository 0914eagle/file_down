
def count_split_weights(n):
    if n == 1:
        return 1
    weights = set()
    for i in range(1, n+1):
        sum_val = 0
        count = 0
        for j in range(i, 0, -1):
            sum_val += j
            count += 1
            if sum_val == n:
                weights.add(count)
            elif sum_val > n:
                break
    return len(weights)

# Input
n = int(input())
print(count_split_weights(n))
```
