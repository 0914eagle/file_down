
def min_total_length(n, m, k, broken_segments):
    if k >= n:
        return n
    diffs = [broken_segments[i+1] - broken_segments[i] - 1 for i in range(n-1)]
    diffs.sort(reverse=True)
    return n + sum(diffs[:k-1])

# Input parsing
n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

# Call the function and print the result
print(min_total_length(n, m, k, broken_segments))
```
