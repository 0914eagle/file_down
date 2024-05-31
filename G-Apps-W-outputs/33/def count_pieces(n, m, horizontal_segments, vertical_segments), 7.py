
def count_pieces(n, m, horizontal_segments, vertical_segments):
    horizontal_events = []
    vertical_events = []
    
    for y, lx, rx in horizontal_segments:
        horizontal_events.append((lx, 1, y))
        horizontal_events.append((rx, -1, y))
        
    for x, ly, ry in vertical_segments:
        vertical_events.append((x, 1, ly, ry))
        
    horizontal_events.sort()
    vertical_events.sort()
    
    horizontal_active = set()
    vertical_active = set()
    num_pieces = 1
    
    for x, event_type, y in horizontal_events:
        if event_type == 1:  # Start of a horizontal segment
            horizontal_active.add(y)
        else:  # End of a horizontal segment
            horizontal_active.remove(y)
        
        num_pieces += len(horizontal_active) + len(vertical_active) - 1
    
    for x, event_type, ly, ry in vertical_events:
        if event_type == 1:  # Start of a vertical segment
            for y in range(ly, ry):
                if y in horizontal_active:
                    num_pieces -= 1
            vertical_active.add((ly, ry))
        else:  # End of a vertical segment
            vertical_active.remove((ly, ry))
    
    return num_pieces

# Input
n, m = map(int, input().split())
horizontal_segments = [list(map(int, input().split())) for _ in range(n)]
vertical_segments = [list(map(int, input().split())) for _ in range(m)]

# Output
print(count_pieces(n, m, horizontal_segments, vertical_segments))
