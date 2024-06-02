
def max_valid_segment_length(n, sushi_types):
    count = {1: 0, 2: 0}
    prefix_count = [{0, 0}]
    for t in sushi_types:
        count[t] += 1
        prefix_count.append({count[1], count[2]})
    
    max_length = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            diff = {prefix_count[j].difference(prefix_count[i-1])}
            if len(diff) == 1 and max(diff) <= (j-i+1) // 2:
                max_length = max(max_length, j-i+1)
    
    return max_length

# Read input
n = int(input())
sushi_types = list(map(int, input().split()))

# Call the function and print the result
print(max_valid_segment_length(n, sushi_types))
