
def count_pieces(n, m, horizontal_segments, vertical_segments):
    events = []
    for y, lx, rx in horizontal_segments:
        events.append((y, lx, 0))
        events.append((y, rx, 1))
    
    for x, ly, ry in vertical_segments:
        events.append((ly, x, 2))
        events.append((ry, x, 3))

    events.sort()

    active_horizontal = set()
    active_vertical = set()
    pieces = 1

    for i in range(len(events) - 1):
        y1, x1, type1 = events[i]
        y2, x2, type2 = events[i + 1]

        if type1 == 0:
            active_horizontal.add(x1)
        elif type1 == 1:
            active_horizontal.remove(x1)
        elif type1 == 2:
            active_vertical.add(x1)
        else:
            active_vertical.remove(x1)

        if type1 < 2:
            if len(active_horizontal) == 0:
                pieces += 1
        else:
            if len(active_horizontal) == 0 and len(active_vertical) == 0:
                pieces += 1

    return pieces

# Input processing
n, m = map(int, input().split())
horizontal_segments = []
for _ in range(n):
    y, lx, rx = map(int, input().split())
    horizontal_segments.append((y, lx, rx))

vertical_segments = []
for _ in range(m):
    x, ly, ry = map(int, input().split())
    vertical_segments.append((x, ly, ry))

# Call the function and print the output
print(count_pieces(n, m, horizontal_segments, vertical_segments))
