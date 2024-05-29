
def check_cloud_cover(n, garry_triangles, m, jerry_triangles):
    garry_set = set()
    jerry_set = set()
    
    for i in range(n):
        tri = sorted(garry_triangles[i])
        garry_set.add(tuple(tri))
        
    for i in range(m):
        tri = sorted(jerry_triangles[i])
        jerry_set.add(tuple(tri))
    
    if garry_set == jerry_set:
        return "yes"
    else:
        return "no"

# Reading input
n = int(input())
garry_triangles = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
jerry_triangles = [list(map(int, input().split())) for _ in range(m)]

# Calling function
result = check_cloud_cover(n, garry_triangles, m, jerry_triangles)
print(result)
