
import sys

def get_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)

def same_cloud_cover(n, garry_triangles, m, jerry_triangles):
    garry_areas = set()
    jerry_areas = set()
    
    for i in range(n):
        area = get_area(*garry_triangles[i])
        garry_areas.add(area)
    
    for i in range(m):
        area = get_area(*jerry_triangles[i])
        jerry_areas.add(area)
    
    if garry_areas == jerry_areas:
        return "yes"
    else:
        return "no"

# Input parsing
lines = sys.stdin.readlines()
n = int(lines[0])
garry_triangles = [list(map(int, lines[i+1].split())) for i in range(n)]
m = int(lines[n+1])
jerry_triangles = [list(map(int, lines[n+i+2].split())) for i in range(m)]

# Function call and output
print(same_cloud_cover(n, garry_triangles, m, jerry_triangles))
