
def are_same_cloud_cover(n, garry_triangles, m, jerry_triangles):
    sorted_garry_triangles = sorted(garry_triangles)
    sorted_jerry_triangles = sorted(jerry_triangles)
    
    if n != m:
        return "no"
    
    for i in range(n):
        if sorted_garry_triangles[i] != sorted_jerry_triangles[i]:
            return "no"
    
    return "yes"

n = int(input())
garry_triangles = []
for _ in range(n):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    garry_triangles.append((x1, y1, x2, y2, x3, y3))

m = int(input())
jerry_triangles = []
for _ in range(m):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    jerry_triangles.append((x1, y1, x2, y2, x3, y3))

print(are_same_cloud_cover(n, garry_triangles, m, jerry_triangles))
```
