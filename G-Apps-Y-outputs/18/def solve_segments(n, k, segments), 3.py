
def solve_segments(n, k, segments):
    count_map = {}
    for i, segment in enumerate(segments):
        l, r = segment
        for j in range(l, r+1):
            if j not in count_map:
                count_map[j] = []
            count_map[j].append(i)
    
    bad_points = []
    for point, covering_segments in count_map.items():
        if len(covering_segments) > k:
            bad_points.append(point)
    
    removed_segments = set()
    for point in bad_points:
        for segment_index in count_map[point]:
            removed_segments.add(segment_index)
    
    print(len(removed_segments))
    print(" ".join(str(index+1) for index in removed_segments))

# Input parsing
n, k = map(int, input().split())
segments = []
for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

solve_segments(n, k, segments)
