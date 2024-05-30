
def min_tape_length(n, m, k, broken_segments):
    lengths = []
    
    for i in range(1, n):
        lengths.append(broken_segments[i] - broken_segments[i-1] - 1)
    
    lengths.sort(reverse=True)
    
    tape_length = n
    for i in range(k-1, n-1):
        tape_length += lengths[i]
    
    return tape_length

n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

print(min_tape_length(n, m, k, broken_segments))
```
