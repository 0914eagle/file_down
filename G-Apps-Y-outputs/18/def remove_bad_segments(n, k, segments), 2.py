
def remove_bad_segments(n, k, segments):
    segment_count = [0] * 201
    bad_points = set()
    bad_segments = set()

    for i, segment in enumerate(segments):
        l, r = segment
        for j in range(l, r+1):
            segment_count[j] += 1
            if segment_count[j] > k:
                bad_points.add(j)
                bad_segments.add(i+1)

    return len(bad_segments), list(bad_segments)

# Input parsing
n, k = map(int, input().split())
segments = []
for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

# Call the function and print the output
result = remove_bad_segments(n, k, segments)
print(result[0])
print(" ".join(str(x) for x in result[1]))
