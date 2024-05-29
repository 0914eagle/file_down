
def find_minimum_tape_length(n, m, k, broken_segments):
    intervals = []
    for i in range(n-1):
        intervals.append(broken_segments[i+1] - broken_segments[i] - 1)
    intervals.sort(reverse=True)
    
    pieces_needed = n
    if k > 1:
        pieces_needed -= k
    
    total_length = sum(intervals[:pieces_needed]) + pieces_needed
    return total_length


# Input reading
n, m, k = map(int, input().split())
broken_positions = list(map(int, input().split()))

# Function call and output
print(find_minimum_tape_length(n, m, k, broken_positions))
```
