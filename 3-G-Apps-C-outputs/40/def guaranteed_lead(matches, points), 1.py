
def guaranteed_lead(matches, points):
    max_points = points[0]
    max_count = points.count(max_points)
    
    matches_to_win = 0
    for i in range(1, len(points)):
        if points[i] == max_points:
            continue
        if points[i] + matches_to_win >= max_points:
            matches_to_win += 1
    
    return matches_to_win

# Reading input
n = int(input())
points = list(map(int, input().split()))

# Calculating and printing the result
result = guaranteed_lead(n, points)
print(result)
