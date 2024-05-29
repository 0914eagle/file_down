
def is_same_cloud_cover(garry_triangles, jerry_triangles):
    return set(garry_triangles) == set(jerry_triangles)

# Read input
n = int(input())
garry_triangles = [tuple(map(int, input().split())) for _ in range(n)]
m = int(input())
jerry_triangles = [tuple(map(int, input().split())) for _ in range(m)]

# Check if Garry and Jerry saw the same cloud cover
if is_same_cloud_cover(garry_triangles, jerry_triangles):
    print("yes")
else:
    print("no")
```
