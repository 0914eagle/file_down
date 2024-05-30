
def min_integers_to_insert(n, arr):
    cnt_zeros = 0
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    
    zero_positions = set()
    for i in range(n):
        if prefix_sum[i + 1] in zero_positions:
            cnt_zeros += 1
            zero_positions = set()
        zero_positions.add(prefix_sum[i + 1])
    
    return cnt_zeros

# Input processing
n = int(input())
arr = list(map(int, input().split()))

# Output
print(min_integers_to_insert(n, arr))
```
