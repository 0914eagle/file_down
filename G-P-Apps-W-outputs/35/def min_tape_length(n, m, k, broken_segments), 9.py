
def min_tape_length(n, m, k, broken_segments):
    if n <= k:
        return n
    
    tape_lengths = []
    for i in range(1, n):
        tape_lengths.append(broken_segments[i] - broken_segments[i-1] - 1)
    
    tape_lengths.sort(reverse=True)
    
    total_length = sum(tape_lengths[:k-1]) + k
    return total_length

# Input
n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

# Output
print(min_tape_length(n, m, k, broken_segments))
```
