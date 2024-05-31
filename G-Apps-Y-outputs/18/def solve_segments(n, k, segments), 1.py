
def solve_segments(n, k, segments):
    points_count = [0] * 201
    segments_cover = [[] for _ in range(201)]
    
    for i, (l, r) in enumerate(segments):
        for j in range(l, r+1):
            points_count[j] += 1
            segments_cover[j].append(i+1)
    
    bad_points = [i for i in range(1, 201) if points_count[i] > k]
    
    removed_segments = set()
    for point in bad_points:
        for segment_idx in segments_cover[point]:
            removed_segments.add(segment_idx)
    
    return len(removed_segments), list(removed_segments)

# Input processing
n, k = map(int, input().split())
segments = []
for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

# Solve the problem
m, removed_segments = solve_segments(n, k, segments)

# Output the result
print(m)
print(" ".join(map(str, removed_segments)))
