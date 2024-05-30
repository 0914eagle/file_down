
def min_tape_length(n, m, k, broken_segments):
    lengths = []
    for i in range(1, n):
        lengths.append(broken_segments[i] - broken_segments[i-1] - 1)
    
    lengths.sort(reverse=True)
    total_length = sum(lengths[:k-1])
    
    return total_length + n

# Input reading and function call
n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

result = min_tape_length(n, m, k, broken_segments)
print(result)
