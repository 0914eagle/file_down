
def check_self_intersections(n, points):
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            if points[i] > points[j] and points[i + 1] < points[j + 1] and points[i] + points[i + 1] > points[j] + points[j + 1]:
                return "yes"
    return "no"

# Read input
n = int(input())
points = list(map(int, input().split()))

# Call the function and print the result
print(check_self_intersections(n, points))
