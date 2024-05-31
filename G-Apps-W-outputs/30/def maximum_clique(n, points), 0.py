
def maximum_clique(n, points):
    points.sort(key=lambda x: x[0])  # Sort points by coordinate
    max_clique = [1]  # Initialize with the first point being a clique of size 1
    
    for i in range(1, n):
        max_w = 0
        for j in range(i):
            if abs(points[i][0] - points[j][0]) >= points[i][1] + points[j][1]:
                max_w = max(max_w, max_clique[j])
        max_clique.append(max_w + 1)
    
    return max(max_clique)

# Input
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

# Output
print(maximum_clique(n, points))
