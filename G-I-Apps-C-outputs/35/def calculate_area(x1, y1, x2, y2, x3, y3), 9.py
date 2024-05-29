
def calculate_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

def is_same_cloud_cover(n, garrys_triangles, m, jerrys_triangles):
    garry_areas = [calculate_area(*triangle) for triangle in garrys_triangles]
    jerry_areas = [calculate_area(*triangle) for triangle in jerrys_triangles]
    
    garry_areas.sort()
    jerry_areas.sort()
    
    return garry_areas == jerry_areas

# Read input
n = int(input())
garrys_triangles = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
jerrys_triangles = [list(map(int, input().split())) for _ in range(m)]

# Check if Garry and Jerry saw the same cloud cover
if is_same_cloud_cover(n, garrys_triangles, m, jerrys_triangles):
    print("yes")
else:
    print("no")
