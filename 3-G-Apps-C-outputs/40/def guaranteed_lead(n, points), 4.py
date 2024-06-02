
def guaranteed_lead(n, points):
    max_points = points[0]
    max_count = points.count(max_points)
    
    matches = 0
    for i in range(1, n):
        if points[i] == max_points:
            matches += 1
        else:
            break
    
    return matches

# Read input
n = int(input())
points = list(map(int, input().split()))

# Call the function and output the result
result = guaranteed_lead(n, points)
print(result)
