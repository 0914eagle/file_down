
def max_beauty_array(n, x, arr):
    max_sum = 0
    current_sum = 0
    prefix_sums = [0]
    
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        prefix_sums.append(prefix_sums[-1] + num)
    
    max_beauty = max(max_sum, max_sum + x * max(prefix_sums) if x > 0 else max_sum)
    
    return max_beauty

# Input parsing
n, x = map(int, input().split())
arr = list(map(int, input().split()))

# Call function and print result
result = max_beauty_array(n, x, arr)
print(result)
```
