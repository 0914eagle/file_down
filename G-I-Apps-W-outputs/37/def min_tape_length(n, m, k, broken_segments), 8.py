
def min_tape_length(n, m, k, broken_segments):
    lengths = [broken_segments[i] - broken_segments[i-1] - 1 for i in range(1, n)]
    lengths.sort(reverse=True)
    
    total = sum(lengths[:k-1]) + k
    return m - total

# Input processing
n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

# Call the function and print the result
print(min_tape_length(n, m, k, broken_segments))
```
