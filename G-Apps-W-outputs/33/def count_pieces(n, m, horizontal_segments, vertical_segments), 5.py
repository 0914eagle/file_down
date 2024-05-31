
def count_pieces(n, m, horizontal_segments, vertical_segments):
    h_lines = [(y, lx, rx) for y, lx, rx in horizontal_segments]
    v_lines = [(x, ly, ry) for x, ly, ry in vertical_segments]
    
    h_lines.sort()
    v_lines.sort()

    h_intervals = [(0, 10**6)]
    v_intervals = [(0, 10**6)]

    for y, lx, rx in h_lines:
        new_intervals = []
        for start, end in h_intervals:
            if y > start and y < end:
                if lx > start:
                    new_intervals.append((start, lx))
                if rx < end:
                    new_intervals.append((rx, end))
            else:
                new_intervals.append((start, end))
        h_intervals = new_intervals

    for x, ly, ry in v_lines:
        new_intervals = []
        for start, end in v_intervals:
            if x > start and x < end:
                if ly > start:
                    new_intervals.append((start, ly))
                if ry < end:
                    new_intervals.append((ry, end))
            else:
                new_intervals.append((start, end))
        v_intervals = new_intervals

    return len(h_intervals) * len(v_intervals)

# Input
n, m = map(int, input().split())
horizontal_segments = [list(map(int, input().split())) for _ in range(n)]
vertical_segments = [list(map(int, input().split())) for _ in range(m)]

# Output
print(count_pieces(n, m, horizontal_segments, vertical_segments))
