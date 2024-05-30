
def min_total_length(n, m, k, broken_segments):
    if k >= n:
        return n
    intervals = [broken_segments[i] - broken_segments[i-1] for i in range(1, n)]
    intervals.sort()
    return sum(intervals[:n-k])

# Input
n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

# Output
print(min_total_length(n, m, k, broken_segments))
```
