
n, A = map(int, input().split())
dice_values = list(map(int, input().split()))

max_sum = sum(dice_values)

output = []
for i in range(n):
    min_sum = A - (max_sum - dice_values[i])
    max_val = min(dice_values[i], min_sum - 1)
    output.append(dice_values[i] - max_val - 1)

print(*output)
```
