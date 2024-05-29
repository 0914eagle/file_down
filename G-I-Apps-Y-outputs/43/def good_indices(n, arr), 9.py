
def good_indices(n, arr):
    nice_indices = []
    
    total_sum = sum(arr)
    
    for i in range(n):
        if (total_sum - arr[i]) % 2 == 0 and (total_sum - arr[i]) // 2 in arr[:i] + arr[i+1:]:
            nice_indices.append(i+1)
    
    return nice_indices

n = int(input())
arr = list(map(int, input().split()))

nice_indices = good_indices(n, arr)
print(len(nice_indices))
if nice_indices:
    print(*nice_indices)
```
