
def guaranteed_lead(n, points):
    max_points = points[0]
    max_count = points.count(max_points)
    
    if max_count == 1:
        return 0
    
    max_points += 1
    while True:
        max_count = points.count(max_points)
        if max_count == 0:
            break
        max_points += 1
    
    return max_points - points[0]

# Read input
n = int(input())
points = list(map(int, input().split()))

# Call the function and print the output
print(guaranteed_lead(n, points))
