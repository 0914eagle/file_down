
def find_min_length(n, m, k, broken_segments):
    if n <= k:
        return n
    
    gaps = []
    for i in range(1, n):
        gaps.append(broken_segments[i] - broken_segments[i - 1] - 1)
    
    gaps.sort(reverse=True)
    return n + sum(gaps[k-1:])

# Input parsing
n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

result = find_min_length(n, m, k, broken_segments)
print(result)
```
