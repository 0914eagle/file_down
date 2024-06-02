
def guaranteed_lead(n, points):
    max_points = points[0]
    max_count = points.count(max_points)
    
    matches = 0
    for i in range(1, n):
        if points[i] == max_points:
            matches += 1
        elif points[i] > max_points:
            max_points = points[i]
            max_count = 1
            matches = 0
        else:
            break
    
    return matches

# Read input
n = int(input())
points = list(map(int, input().split()))

# Call the function and output the result
print(guaranteed_lead(n, points))
