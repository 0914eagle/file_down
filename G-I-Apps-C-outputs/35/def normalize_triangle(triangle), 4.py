
def normalize_triangle(triangle):
    # Normalize triangle vertices so that the one with the lowest x-coordinate is the first vertex
    x_values = [triangle[0], triangle[2], triangle[4]]
    min_index = x_values.index(min(x_values))
    normalized_triangle = [triangle[min_index*2], triangle[min_index*2+1],
                           triangle[(min_index+1)%3*2], triangle[(min_index+1)%3*2+1],
                           triangle[(min_index+2)%3*2], triangle[(min_index+2)%3*2+1]]
    return normalized_triangle

def are_triangles_equal(triangle1, triangle2):
    # Check if two triangles are equal regardless of vertex order
    triangle1 = normalize_triangle(triangle1)
    triangle2 = normalize_triangle(triangle2)
    return triangle1 == triangle2

def are_clouds_equal(garry_cloud, jerry_cloud):
    # Check if Garry and Jerry saw the same cloud cover
    if len(garry_cloud) != len(jerry_cloud):
        return "no"
    
    for garry_triangle in garry_cloud:
        found_match = False
        for jerry_triangle in jerry_cloud:
            if are_triangles_equal(garry_triangle, jerry_triangle):
                found_match = True
                break
        
        if not found_match:
            return "no"
    
    return "yes"

# Read input
n = int(input())
garry_cloud = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
jerry_cloud = [list(map(int, input().split())) for _ in range(m)]

# Check if Garry and Jerry saw the same cloud cover
print(are_clouds_equal(garry_cloud, jerry_cloud))
```
