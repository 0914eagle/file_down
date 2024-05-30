
def min_integers_to_insert(n, arr):
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    
    count = {}
    for i in range(n + 1):
        if prefix_sum[i] not in count:
            count[prefix_sum[i]] = 1
        else:
            count[prefix_sum[i]] += 1
    
    max_count = max(count.values())
    return n - max_count

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(min_integers_to_insert(n, arr))
```
