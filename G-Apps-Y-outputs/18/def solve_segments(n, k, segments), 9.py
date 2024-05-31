
def solve_segments(n, k, segments):
    bad_points = {}
    segment_count = {}
    removed_segments = []

    for i, segment in enumerate(segments, start=1):
        l, r = segment
        for j in range(l, r+1):
            if j not in bad_points:
                bad_points[j] = 1
            else:
                bad_points[j] += 1

    for point, count in bad_points.items():
        if count > k:
            for i, segment in enumerate(segments, start=1):
                l, r = segment
                if l <= point <= r:
                    if i in segment_count:
                        segment_count[i] += 1
                    else:
                        segment_count[i] = 1

    for segment, count in segment_count.items():
        if count > k:
            removed_segments.append(segment)

    return len(removed_segments), removed_segments


# Input
n, k = map(int, input().split())
segments = []
for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

# Output
m, removed_segments = solve_segments(n, k, segments)
print(m)
print(*removed_segments)
