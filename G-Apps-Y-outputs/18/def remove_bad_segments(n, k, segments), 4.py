
def remove_bad_segments(n, k, segments):
    bad_points = {}
    for i, (l, r) in enumerate(segments):
        for j in range(l, r + 1):
            if j in bad_points:
                bad_points[j].append(i)
            else:
                bad_points[j] = [i]

    count = {}
    for point, segments in bad_points.items():
        if len(segments) > k:
            for segment in segments:
                count[segment] = count.get(segment, 0) + 1

    to_remove = []
    for segment, freq in count.items():
        if freq > k:
            to_remove.append(segment)

    return len(to_remove), to_remove

# Read input
n, k = map(int, input().split())
segments = [list(map(int, input().split())) for _ in range(n)]

# Call the function and print the output
m, removed_segments = remove_bad_segments(n, k, segments)
print(m)
print(*removed_segments)
