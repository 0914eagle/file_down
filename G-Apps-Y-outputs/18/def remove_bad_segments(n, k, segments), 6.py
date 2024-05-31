
def remove_bad_segments(n, k, segments):
    bad_points = {}
    for i in range(1, 201):
        bad_points[i] = 0

    for segment in segments:
        for j in range(segment[0], segment[1] + 1):
            bad_points[j] += 1

    to_remove = []
    for i, segment in enumerate(segments):
        bad_count = sum(1 for j in range(segment[0], segment[1] + 1) if bad_points[j] > k)
        if bad_count > 0:
            to_remove.append(i + 1)

    return len(to_remove), to_remove

# Input parsing
n, k = map(int, input().split())
segments = []
for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

# Call the function and output the result
m, removed_segments = remove_bad_segments(n, k, segments)
print(m)
print(" ".join(map(str, removed_segments)))
