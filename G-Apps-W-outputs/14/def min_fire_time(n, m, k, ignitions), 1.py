
def min_fire_time(n, m, k, ignitions):
    max_dist = 0
    for i in range(k):
        for j in range(i + 1, k):
            dist = max(abs(ignitions[i][0] - ignitions[j][0]), abs(ignitions[i][1] - ignitions[j][1]))
            max_dist = max(max_dist, dist)
    
    max_dist = max(max_dist, max(ignitions[0][0] - 1, n - ignitions[-1][0]))
    max_dist = max(max_dist, max(ignitions[0][1] - 1, m - ignitions[-1][1]))
    
    return (max_dist + 1) // 2

# Input parsing
n, m, k = map(int, input().split())
ignitions = [tuple(map(int, input().split())) for _ in range(k)]

# Call the function and print the output
print(min_fire_time(n, m, k, ignitions))
