
def solve_segments(n, k, segments):
    bad_points = {}
    for i, (l, r) in enumerate(segments):
        for j in range(l, r + 1):
            if j in bad_points:
                if len(bad_points[j]) < k:
                    bad_points[j].append(i + 1)  # 1-indexed segment numbers
            else:
                bad_points[j] = [i + 1]

    to_remove = set()
    for points in bad_points.values():
        if len(points) > k:
            to_remove.update(points[k:])

    return len(to_remove), list(to_remove)

# Input parsing
n, k = map(int, input().split())
segments = []
for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

# Solve and print output
m, segments_to_remove = solve_segments(n, k, segments)
print(m)
print(" ".join(map(str, segments_to_remove)))
