
def min_tape_length(n, m, k, broken_segments):
    if k >= n:
        return n
    
    intervals = []
    for i in range(1, n):
        intervals.append(broken_segments[i] - broken_segments[i-1] - 1)
    
    intervals.sort(reverse=True)
    
    total_length = n
    for i in range(k-1, n):
        total_length += intervals[i]
    
    return total_length

# Input parsing
n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

# Call the function and output the result
print(min_tape_length(n, m, k, broken_segments))
```
