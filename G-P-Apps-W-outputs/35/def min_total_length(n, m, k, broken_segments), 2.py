
def min_total_length(n, m, k, broken_segments):
    gaps = []
    
    for i in range(1, n):
        gaps.append(broken_segments[i] - broken_segments[i-1] - 1)
    
    gaps.sort(reverse=True)
    
    total_length = broken_segments[-1] - broken_segments[0] + 1
    
    for i in range(k-1):
        if i < len(gaps):
            total_length -= gaps[i]
    
    return total_length

# Read input
n, m, k = map(int, input().split())
broken_segments = list(map(int, input().split()))

# Call the function and print the result
print(min_total_length(n, m, k, broken_segments))
