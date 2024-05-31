
def count_pieces(n, m, horizontal_segments, vertical_segments):
    events = []
    for y, lx, rx in horizontal_segments:
        events.append((y, lx, rx, 'h'))
        events.append((y, lx, rx, 'h_end'))

    for x, ly, ry in vertical_segments:
        events.append((ly, x, y, 'v'))
        events.append((ry, x, y, 'v_end'))

    events.sort()

    active_h = []
    active_v = []
    pieces = 1

    for y, x1, x2, event_type in events:
        if event_type == 'h':
            active_h.append((x1, x2))
            active_h.sort()
        elif event_type == 'h_end':
            active_h.remove((x1, x2))
        elif event_type == 'v':
            active_v.append((x1, x2))
            active_v.sort()
        elif event_type == 'v_end':
            active_v.remove((x1, x2))

        if len(active_h) == 0 or len(active_v) == 0:
            pieces += 1
        else:
            x_range = (active_h[0][0], active_h[-1][1])
            y_range = (active_v[0][0], active_v[-1][1])
            if x_range[0] < x_range[1] and y_range[0] < y_range[1]:
                pieces += 1

    return pieces

n, m = map(int, input().split())
horizontal_segments = [list(map(int, input().split())) for _ in range(n)]
vertical_segments = [list(map(int, input().split())) for _ in range(m)]

result = count_pieces(n, m, horizontal_segments, vertical_segments)
print(result)
