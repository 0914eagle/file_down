
def count_pieces(n, m, horizontal_segments, vertical_segments):
    events = []
    for y, lx, rx in horizontal_segments:
        events.append((y, lx, rx, 0))
        events.append((y, lx, rx, 1))
    
    for x, ly, ry in vertical_segments:
        events.append((x, ly, ry, 0))
        events.append((x, ly, ry, 1))
    
    events.sort()
    
    active_segments = set()
    count = 1
    
    for i in range(len(events) - 1):
        y, l, r, is_end = events[i]
        if is_end == 0:
            active_segments.add((l, r))
        else:
            active_segments.remove((l, r))
        
        count += 1 + len(active_segments)
    
    return count

# Input
n, m = map(int, input().split())
horizontal_segments = [list(map(int, input().split())) for _ in range(n)]
vertical_segments = [list(map(int, input().split())) for _ in range(m)]

# Output
print(count_pieces(n, m, horizontal_segments, vertical_segments))
