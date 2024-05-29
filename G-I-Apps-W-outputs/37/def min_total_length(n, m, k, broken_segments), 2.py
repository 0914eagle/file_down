
def min_total_length(n, m, k, broken_segments):
    if n <= k:
        return n
    intervals = []
    for i in range(1, n):
        intervals.append(broken_segments[i] - broken_segments[i-1] - 1)
    intervals.sort()
    return sum(intervals[:n-k])

# Input
n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

# Output
print(min_total_length(n, m, k, broken_segments))
```