
def count_square_pieces(n, m, horizontal_segments, vertical_segments):
    horizontal_segments.sort()
    vertical_segments.sort()
    
    horizontal_points = set()
    vertical_points = set()
    
    for seg in horizontal_segments:
        horizontal_points.add(seg[1])
        horizontal_points.add(seg[2])
    
    for seg in vertical_segments:
        vertical_points.add(seg[1])
        vertical_points.add(seg[2])
    
    horizontal_points = list(horizontal_points)
    vertical_points = list(vertical_points)
    horizontal_points.sort()
    vertical_points.sort()
    
    h_count = len(horizontal_points)
    v_count = len(vertical_points)
    
    h_map = {val: i for i, val in enumerate(horizontal_points)}
    v_map = {val: i for i, val in enumerate(vertical_points)}
    
    grid = [[0 for _ in range(v_count - 1)] for _ in range(h_count - 1)]
    
    for seg in horizontal_segments:
        x, y1, y2 = seg
        y1_idx = h_map[y1]
        y2_idx = h_map[y2]
        for i in range(y1_idx, y2_idx):
            grid[x-1][i] = 1
    
    for seg in vertical_segments:
        y, x1, x2 = seg
        x1_idx = v_map[x1]
        x2_idx = v_map[x2]
        for i in range(x1_idx, x2_idx):
            grid[i][y-1] = 1
    
    pieces = 0
    for i in range(h_count - 1):
        for j in range(v_count - 1):
            if grid[i][j] == 0:
                pieces += 1
    
    return pieces

# Input reading
n, m = map(int, input().split())
horizontal_segments = []
vertical_segments = []
for _ in range(n):
    y, lx, rx = map(int, input().split())
    horizontal_segments.append((y, lx, rx))
for _ in range(m):
    x, ly, ry = map(int, input().split())
    vertical_segments.append((x, ly, ry))

result = count_square_pieces(n, m, horizontal_segments, vertical_segments)
print(result)
