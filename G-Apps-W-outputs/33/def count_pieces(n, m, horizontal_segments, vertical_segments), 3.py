
def count_pieces(n, m, horizontal_segments, vertical_segments):
    vertical_points = set()
    horizontal_points = set()

    for i in range(n):
        y, lx, rx = horizontal_segments[i]
        horizontal_points.add((y, lx, rx))

    for i in range(m):
        x, ly, ry = vertical_segments[i]
        vertical_points.add((x, ly, ry))

    vertical_points = sorted(list(vertical_points))
    horizontal_points = sorted(list(horizontal_points))

    num_pieces = 1
    for x, ly, ry in vertical_points:
        start = 0
        for y, lx, rx in horizontal_points:
            if lx <= x <= rx and ly <= y <= ry:
                num_pieces += 1
            if ly <= y <= ry:
                if start == 0:
                    num_pieces += 1
                start = 1
            else:
                start = 0

    return num_pieces

n, m = map(int, input().split())
horizontal_segments = [list(map(int, input().split())) for _ in range(n)]
vertical_segments = [list(map(int, input().split())) for _ in range(m)]

result = count_pieces(n, m, horizontal_segments, vertical_segments)
print(result)
