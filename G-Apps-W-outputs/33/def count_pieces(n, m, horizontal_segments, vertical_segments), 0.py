
def count_pieces(n, m, horizontal_segments, vertical_segments):
    intersections = set()
    
    for y, lx, rx in horizontal_segments:
        intersections.add((y, lx, "l"))
        intersections.add((y, rx, "r"))
        
    for x, ly, ry in vertical_segments:
        intersections.add((ly, x, "d"))
        intersections.add((ry, x, "u"))
    
    intersections = sorted(list(intersections))
    
    pieces = 1
    
    for i in range(1, len(intersections)):
        prev_y, prev_x, prev_type = intersections[i-1]
        curr_y, curr_x, curr_type = intersections[i]
        
        if prev_type == "l" and curr_type == "l":
            pieces += 1
        elif prev_type == "r" and curr_type == "r":
            pieces += 1
        elif prev_type == "d" and curr_type == "d":
            pieces += 1
        elif prev_type == "u" and curr_type == "u":
            pieces += 1
        elif prev_type == "l" and curr_type == "r":
            pieces -= 1
        elif prev_type == "d" and curr_type == "u":
            pieces -= 1
    
    return pieces

# Input
n, m = map(int, input().split())
horizontal_segments = [list(map(int, input().split())) for _ in range(n)]
vertical_segments = [list(map(int, input().split())) for _ in range(m)]

# Output
print(count_pieces(n, m, horizontal_segments, vertical_segments))
