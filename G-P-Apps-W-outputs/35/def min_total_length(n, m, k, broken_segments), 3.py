
def min_total_length(n, m, k, broken_segments):
    if k >= n:
        return n
    
    diff = []
    for i in range(1, n):
        diff.append(broken_segments[i] - broken_segments[i-1] - 1)
    
    diff.sort(reverse=True)
    
    total_length = n
    for i in range(k-1, n-1):
        total_length += diff[i]
    
    return total_length

# Input
n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

# Output
print(min_total_length(n, m, k, broken_segments))
```
