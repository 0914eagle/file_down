
def guaranteed_lead(matches, points):
    julia_points = points[0]
    max_points = max(points)
    count = 0

    for i in range(1, matches):
        if julia_points + matches - i <= max_points:
            break
        count += 1

    return count

# Input
n = int(input())
points = list(map(int, input().split()))

# Output
print(guaranteed_lead(n, points))
