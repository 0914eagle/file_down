
def find_nice_indices(n, arr):
    nice_indices = []
    
    total_sum = sum(arr)
    
    for i in range(n):
        if (total_sum - arr[i]) % 2 == 0:
            half_sum = (total_sum - arr[i]) // 2
            if half_sum in arr[:i] + arr[i+1:]:
                nice_indices.append(i+1)
    
    k = len(nice_indices)
    
    print(k)
    if k > 0:
        print(" ".join(map(str, nice_indices)))

# Input parsing
n = int(input())
arr = list(map(int, input().split()))

# Call the function
find_nice_indices(n, arr)
```
