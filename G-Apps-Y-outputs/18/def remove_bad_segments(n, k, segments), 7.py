
def remove_bad_segments(n, k, segments):
    bad_points = {}
    for i in range(n):
        l, r = segments[i]
        for j in range(l, r + 1):
            if j in bad_points:
                bad_points[j] += 1
            else:
                bad_points[j] = 1

    to_remove = []
    for i in range(n):
        l, r = segments[i]
        for j in range(l, r + 1):
            if bad_points[j] > k:
                to_remove.append(i+1)
                break

    return len(to_remove), to_remove

# Input
n, k = map(int, input().split())
segments = [list(map(int, input().split())) for _ in range(n)]

# Output
m, removed_segments = remove_bad_segments(n, k, segments)
print(m)
print(' '.join(map(str, removed_segments)))
