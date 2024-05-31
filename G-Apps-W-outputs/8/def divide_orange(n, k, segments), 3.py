
def divide_orange(n, k, segments):
    result = []
    for i in range(k):
        child_segments = []
        for j in range(n):
            child_segments.append(i*n + j + 1)
        result.append(child_segments)
    
    output = []
    for i in range(n):
        for j in range(k):
            output.append(result[j][i])
    
    return output

# Input
n, k = map(int, input().split())
segments = list(map(int, input().split()))

# Output
output_segments = divide_orange(n, k, segments)
print(*output_segments)
