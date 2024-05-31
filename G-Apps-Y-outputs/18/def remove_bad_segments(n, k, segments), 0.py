
def remove_bad_segments(n, k, segments):
    bad_points = {}
    for i, (l, r) in enumerate(segments):
        for j in range(l, r + 1):
            if j not in bad_points:
                bad_points[j] = []
            bad_points[j].append(i)

    bad_segments = set()
    for point, covering_segments in bad_points.items():
        if len(covering_segments) > k:
            for segment_idx in covering_segments:
                bad_segments.add(segment_idx)

    return len(bad_segments), list(bad_segments)


# Reading input
n, k = map(int, input().split())
segments = []
for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

# Solving the problem
removed_segments_count, removed_segments_indices = remove_bad_segments(n, k, segments)

# Printing output
print(removed_segments_count)
print(" ".join(str(i + 1) for i in removed_segments_indices))
