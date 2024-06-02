
def check_self_intersections(n, points):
    points.sort()
    
    for i in range(n - 2):
        if points[i] < points[i + 1] and points[i + 1] < points[i + 2]:
            return "yes"
    
    return "no"

# Input
n = int(input())
points = list(map(int, input().split()))

# Output
print(check_self_intersections(n, points))
