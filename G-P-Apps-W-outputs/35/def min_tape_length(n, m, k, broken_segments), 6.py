
def min_tape_length(n, m, k, broken_segments):
    diffs = []
    for i in range(1, n):
        diffs.append(broken_segments[i] - broken_segments[i-1] - 1)

    diffs.sort(reverse=True)

    total_length = broken_segments[-1] - broken_segments[0] + 1
    for i in range(k-1):
        total_length -= diffs[i]

    return total_length

# Input parsing
n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

# Call the function and print the result
print(min_tape_length(n, m, k, broken_segments))
```
