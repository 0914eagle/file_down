
def max_expression_value(n, a):
    prefix_sum = [0] * (n + 1)
    suffix_sum = [0] * (n + 2)
    
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]
    
    for i in range(n, 0, -1):
        suffix_sum[i] = suffix_sum[i + 1] + a[i - 1]
    
    max_val = 0
    for k in range(1, n + 1):
        max_val = max(max_val, prefix_sum[k] ** 2 * suffix_sum[k + 1])
    
    return max_val

# Reading input
n = int(input())
a = [int(input()) for _ in range(n)]

# Output where expression value is maximal
print(max_expression_value(n, a))
```
