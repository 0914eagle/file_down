
def max_value_of_expression(n, integers):
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + integers[i - 1]

    max_value = 0
    for k in range(1, n):
        value = (prefix_sum[k] ** 2) * (prefix_sum[n] - prefix_sum[k])
        max_value = max(max_value, value)
    
    return max_value

# Input parsing
n = int(input())
integers = []
for _ in range(n):
    integers.append(int(input()))

# Output the result
print(max_value_of_expression(n, integers))
```
