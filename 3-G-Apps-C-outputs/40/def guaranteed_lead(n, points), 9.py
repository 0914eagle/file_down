
def guaranteed_lead(n, points):
    max_points = points[0]
    max_count = 1
    for i in range(1, n):
        if points[i] == max_points:
            max_count += 1
        else:
            break
    return max_count

# Read input
n = int(input())
points = list(map(int, input().split()))

# Calculate and output the result
result = guaranteed_lead(n, points)
print(result)
