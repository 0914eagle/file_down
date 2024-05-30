
def min_integers_to_insert(n, arr):
    count = 0
    prefix_sum = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    
    prefix_sum_set = set()
    
    for i in range(1, n + 1):
        if prefix_sum[i] in prefix_sum_set:
            count += 1
            prefix_sum_set = set()
            prefix_sum_set.add(prefix_sum[i - 1])
        
        prefix_sum_set.add(prefix_sum[i])
    
    return count

n = int(input())
arr = list(map(int, input().split()))

print(min_integers_to_insert(n, arr))
```
