
def are_same_cloud_cover(n, garry_triangles, m, jerry_triangles):
    def normalize_triangle(triangle):
        return tuple(sorted(triangle))

    garry_set = set()
    for _ in range(n):
        triangle = [tuple(sorted(map(int, input().split()))) for _ in range(3)]
        garry_set.add(normalize_triangle(triangle))

    jerry_set = set()
    for _ in range(m):
        triangle = [tuple(sorted(map(int, input().split()))) for _ in range(3)]
        jerry_set.add(normalize_triangle(triangle))

    return "yes" if garry_set == jerry_set else "no"

n = int(input())
garry_triangles = []
m = int(input())
jerry_triangles = []

print(are_same_cloud_cover(n, garry_triangles, m, jerry_triangles))
```
