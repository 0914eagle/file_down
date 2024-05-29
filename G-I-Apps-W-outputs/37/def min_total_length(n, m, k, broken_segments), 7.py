
def min_total_length(n, m, k, broken_segments):
    if k >= n:
        return n

    intervals = [broken_segments[i] - broken_segments[i - 1] for i in range(1, n)]
    intervals.sort(reverse=True)

    total_length = n
    for i in range(k - 1, len(intervals)):
        total_length += intervals[i] - 1

    return total_length

# Input
n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

print(min_total_length(n, m, k, broken_segments))
```
