
def max_value(n, values):
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + values[i - 1]
    
    max_val = 0
    for k in range(1, n):
        curr_val = (prefix_sum[k] ** 2) * (prefix_sum[n] - prefix_sum[k])
        max_val = max(max_val, curr_val)
    
    return max_val

n = int(input())
values = []
for _ in range(n):
    values.append(int(input()))

result = max_value(n, values)
print(result)
```
