
def are_same_cloud_cover(notes1, notes2):
    def are_triangles_equal(triangle1, triangle2):
        return set(triangle1) == set(triangle2)

    triangles1 = [tuple(map(int, notes1[i].split())) for i in range(notes1)]
    triangles2 = [tuple(map(int, notes2[i].split())) for i in range(notes2)]

    return "yes" if sorted(triangles1, key=lambda x: tuple(sorted(x))) == sorted(triangles2, key=lambda x: tuple(sorted(x))) else "no"

n = int(input())
garry_notes = [input() for _ in range(n)]
m = int(input())
jerry_notes = [input() for _ in range(m)]

print(are_same_cloud_cover(n, garry_notes, m, jerry_notes))
```
