
def min_integers_to_insert(n, arr):
    zero_subsegments = 0
    prefix_sums = [0] * n
    prefix_sums[0] = arr[0]
    
    for i in range(1, n):
        prefix_sums[i] = prefix_sums[i-1] + arr[i]
        if prefix_sums[i] == 0:
            zero_subsegments += 1
            
    return zero_subsegments

# Input parsing
n = int(input())
arr = list(map(int, input().split()))

result = min_integers_to_insert(n, arr)
print(result)
```
