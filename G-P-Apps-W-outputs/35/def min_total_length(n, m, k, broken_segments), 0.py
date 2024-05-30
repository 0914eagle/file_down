
def min_total_length(n, m, k, broken_segments):
    intervals = [broken_segments[0]-1]  # Add the leftmost non-broken segment
    for i in range(1, n):
        intervals.append(broken_segments[i] - broken_segments[i-1] - 1)
    intervals.append(m - broken_segments[-1])  # Add the rightmost non-broken segment

    intervals.sort(reverse=True)
    return sum(intervals[k-1:])

# Input reading
n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

# Call the function and print the result
print(min_total_length(n, m, k, broken_segments))
```
