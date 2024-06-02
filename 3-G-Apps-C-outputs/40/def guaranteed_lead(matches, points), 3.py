
def guaranteed_lead(matches, points):
    max_points = points[0]
    max_count = points.count(max_points)
    
    guaranteed_matches = 0
    for i in range(1, len(points)):
        if points[i] == max_points:
            guaranteed_matches += 1
        else:
            break
    
    return guaranteed_matches

# Read input
n = int(input())
points = list(map(int, input().split()))

# Calculate and output result
result = guaranteed_lead(n, points)
print(result)
