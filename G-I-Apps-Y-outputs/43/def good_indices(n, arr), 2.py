
def good_indices(n, arr):
    prefix_sum = sum(arr)
    value_count = {}
    for i, num in enumerate(arr):
        if prefix_sum - num in value_count:
            value_count[prefix_sum - num].append(i+1)
        else:
            value_count[prefix_sum - num] = [i+1]
    
    nice_indices = []
    for i, num in enumerate(arr):
        if num in value_count and len(value_count[num]) > 1:
            nice_indices.append(i+1)
        elif num in value_count and len(value_count[num]) == 1 and value_count[num][0] != i+1:
            nice_indices.append(i+1)
    
    return len(nice_indices), nice_indices

# Input handling
n = int(input())
arr = list(map(int, input().split()))

k, indices = good_indices(n, arr)
print(k)
if k > 0:
    print(*indices)
```
