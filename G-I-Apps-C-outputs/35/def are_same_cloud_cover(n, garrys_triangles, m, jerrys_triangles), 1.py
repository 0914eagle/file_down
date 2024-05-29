
def are_same_cloud_cover(n, garrys_triangles, m, jerrys_triangles):
    def normalize(triangle):
        return tuple(sorted(triangle))
    
    garrys_cloud_cover = set()
    jerrys_cloud_cover = set()
    
    for _ in range(n):
        x1, y1, x2, y2, x3, y3 = garrys_triangles[_]
        garrys_cloud_cover.add(normalize([(x1, y1), (x2, y2), (x3, y3)])
    
    for _ in range(m):
        x1, y1, x2, y2, x3, y3 = jerrys_triangles[_]
        jerrys_cloud_cover.add(normalize([(x1, y1), (x2, y2), (x3, y3)])
    
    return "yes" if garrys_cloud_cover == jerrys_cloud_cover else "no"

# Read input
n = int(input())
garrys_triangles = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
jerrys_triangles = [list(map(int, input().split())) for _ in range(m)]

# Check if Garry and Jerry saw the same cloud cover
result = are_same_cloud_cover(n, garrys_triangles, m, jerrys_triangles)
print(result)
```
