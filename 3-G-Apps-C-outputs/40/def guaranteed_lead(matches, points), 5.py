
def guaranteed_lead(matches, points):
    max_points = points[0]
    count = 0
    
    for i in range(1, len(points)):
        if points[i] == max_points:
            count += 1
        else:
            break
    
    return count

# Input
n = int(input())
points = list(map(int, input().split()))

# Output
print(guaranteed_lead(n, points))
