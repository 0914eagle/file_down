
def remove_bad_segments(n, k, segments):
    bad_points = {}
    for i, (l, r) in enumerate(segments):
        for j in range(l, r+1):
            if j in bad_points:
                bad_points[j].append(i)
            else:
                bad_points[j] = [i]

    to_remove = set()
    for points in bad_points.values():
        if len(points) > k:
            to_remove.update(points)

    return len(to_remove), sorted(list(to_remove, reverse=True))


# Read input
n, k = map(int, input().split())
segments = [list(map(int, input().split())) for _ in range(n)]

# Call the function
result = remove_bad_segments(n, k, segments)

# Print output
print(result[0])
print(" ".join(map(str, result[1])))
