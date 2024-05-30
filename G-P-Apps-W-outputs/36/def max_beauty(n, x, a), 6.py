
def max_beauty(n, x, a):
    max_sum = 0
    current_sum = 0
    prefix_sum = []
    
    for num in a:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        prefix_sum.append(max_sum)
    
    suffix_sum = []
    current_sum = 0
    max_sum = 0
    for num in a[::-1]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        suffix_sum.append(max_sum)
    
    suffix_sum = suffix_sum[::-1]
    
    result = 0
    for i in range(n):
        result = max(result, a[i])
        if i > 0:
            result = max(result, prefix_sum[i-1] + a[i]*x)
        if i < n-1:
            result = max(result, suffix_sum[i+1] + a[i]*x)
    
    return result

# Input processing
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Call the function and print the result
print(max_beauty(n, x, a))
```
