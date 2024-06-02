
def guaranteed_lead(n, points):
    max_points = max(points)
    count = 0
    for i in range(n):
        if points[i] == max_points:
            count += 1
    return count

# Read input
n = int(input())
points = list(map(int, input().split()))

# Calculate and output the result
result = guaranteed_lead(n, points)
print(result)
