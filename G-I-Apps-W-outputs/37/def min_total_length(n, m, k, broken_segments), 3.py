
def min_total_length(n, m, k, broken_segments):
    gaps = []
    for i in range(1, n):
        gap_length = broken_segments[i] - broken_segments[i-1] - 1
        if gap_length > 0:
            gaps.append(gap_length)
    
    gaps.sort(reverse=True)
    
    total_length = sum(gaps) + n
    for i in range(k-1):
        if i < len(gaps):
            total_length -= gaps[i] - 1
    
    return total_length

n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

print(min_total_length(n, m, k, broken_segments))
```
