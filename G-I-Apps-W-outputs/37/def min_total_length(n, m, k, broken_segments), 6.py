
def min_total_length(n, m, k, broken_segments):
    if n <= k:
        return n
    
    intervals = []
    
    for i in range(1, n):
        intervals.append(broken_segments[i] - broken_segments[i-1] - 1)
    
    intervals.sort(reverse=True)
    
    total_length = broken_segments[-1] - broken_segments[0] + 1
    
    for i in range(k-1):
        total_length -= intervals[i]
    
    return total_length

# Input parsing
n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

# Call the function and print the output
print(min_total_length(n, m, k, broken_segments))
```
