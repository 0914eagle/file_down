
def count_weights(n):
    if n == 1:
        return 1
    weights = set()
    for i in range(1, int(n**0.5) + 1):
        remaining_sum = n
        current_num = i
        while remaining_sum >= current_num:
            weights.add(remaining_sum)
            remaining_sum -= current_num
            current_num += 1
    return len(weights) + 1

# Input
n = int(input().strip())

# Output
print(count_weights(n))
```
