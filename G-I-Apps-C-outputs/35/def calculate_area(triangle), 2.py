
def calculate_area(triangle):
    x1, y1, x2, y2, x3, y3 = triangle
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

def normalize_triangle(triangle):
    x1, y1, x2, y2, x3, y3 = triangle
    return tuple(sorted([x1, y1, x2, y2, x3, y3]))

def normalize_triangles(triangles):
    return [normalize_triangle(triangle) for triangle in triangles]

def same_cloud_cover(garry_triangles, jerry_triangles):
    normalized_garry_triangles = normalize_triangles(garry_triangles)
    normalized_jerry_triangles = normalize_triangles(jerry_triangles)
    
    normalized_garry_triangles.sort()
    normalized_jerry_triangles.sort()
    
    return normalized_garry_triangles == normalized_jerry_triangles

def main():
    n = int(input())
    garry_triangles = [tuple(map(int, input().split())) for _ in range(n)]
    m = int(input())
    jerry_triangles = [tuple(map(int, input().split())) for _ in range(m)]
    
    if same_cloud_cover(garry_triangles, jerry_triangles):
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()
