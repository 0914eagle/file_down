
def count_pieces(n, m, horizontal_segments, vertical_segments):
    horizontal_points = set()
    vertical_points = set()
    
    for y, lx, rx in horizontal_segments:
        horizontal_points.add((lx, y))
        horizontal_points.add((rx, y))
    
    for x, ly, ry in vertical_segments:
        vertical_points.add((x, ly))
        vertical_points.add((x, ry))
    
    horizontal_points = sorted(list(horizontal_points))
    vertical_points = sorted(list(vertical_points))
    
    horizontal_cuts = [0]
    for i in range(1, len(horizontal_points)):
        if horizontal_points[i][1] != horizontal_points[i-1][1]:
            horizontal_cuts.append(horizontal_points[i][0])
    
    vertical_cuts = [0]
    for i in range(1, len(vertical_points)):
        if vertical_points[i][1] != vertical_points[i-1][1]:
            vertical_cuts.append(vertical_points[i][0])
    
    return (len(horizontal_cuts) * len(vertical_cuts)) % (10**9 + 7)

# Input
n, m = map(int, input().split())
horizontal_segments = [map(int, input().split()) for _ in range(n)]
vertical_segments = [map(int, input().split()) for _ in range(m)]

# Output
print(count_pieces(n, m, horizontal_segments, vertical_segments))
