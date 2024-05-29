
def max_value(n, a):
    max_sum = 0
    prefix_sum = [0] * n
    prefix_sum[0] = a[0]
    
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + a[i]
    
    for i in range(1, n):
        cur_sum = prefix_sum[i-1] * (prefix_sum[n-1] - prefix_sum[i-1])
        if cur_sum > max_sum:
            max_sum = cur_sum
    
    return max_sum

# Read input
n = int(input())
a = [int(input()) for _ in range(n)]

# Get maximal value and output result
result = max_value(n, a)
print(result)
```
