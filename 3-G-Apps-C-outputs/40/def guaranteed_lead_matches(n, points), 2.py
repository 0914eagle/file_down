
def guaranteed_lead_matches(n, points):
    max_points = points[0]
    max_count = 1
    for i in range(1, n):
        if points[i] == max_points:
            max_count += 1
        else:
            break
    return max_count

# Input
n = int(input())
points = list(map(int, input().split()))

# Output
print(guaranteed_lead_matches(n, points))
