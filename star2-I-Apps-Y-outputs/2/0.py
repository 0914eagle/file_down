
n, m = map(int, input().split())
a = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

def calc_max_diff(a, segments):
    min_val, max_val = 10**6 + 1, -10**6 - 1
    for l, r in segments:
        min_val = min(min_val, a[l - 1])
        max_val = max(max_val, a[l - 1])
    return max_val - min_val

max_diff = 0
max_segments = []
for i in range(1, 2**m):
    segments_mask = bin(i)[2:].zfill(m)
    segments_to_apply = [segments[j] for j in range(m) if segments_mask[j] == '1']
    diff = calc_max_diff(a, segments_to_apply)
    if diff > max_diff:
        max_diff = diff
        max_segments = segments_to_apply

print(max_diff)
print(len(max_segments))
print(' '.join(str(segments.index(s) + 1) for s in max_segments))

