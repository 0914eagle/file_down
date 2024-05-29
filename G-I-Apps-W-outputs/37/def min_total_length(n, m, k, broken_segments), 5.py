
def min_total_length(n, m, k, broken_segments):
    intervals = [broken_segments[i] - broken_segments[i-1] - 1 for i in range(1, n)]
    intervals.sort(reverse=True)
    return sum(intervals[:k-1]) + n

# Input parsing
n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

result = min_total_length(n, m, k, broken_segments)
print(result)
```
