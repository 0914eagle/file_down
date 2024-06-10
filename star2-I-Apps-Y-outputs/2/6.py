
n, m = map(int, input().split())
a = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

def calc_diff(a, segments):
    min_val = float('inf')
    max_val = float('-inf')
    for l, r in segments:
        min_val = min(min_val, a[l-1])
        max_val = max(max_val, a[l-1])
    return max_val - min_val

def solve(a, segments):
    best_diff = 0
    best_segments = []
    for mask in range(1 << len(segments)):
        cur_segments = []
        for i in range(len(segments)):
            if mask & (1 << i):
                cur_segments.append(segments[i])
        cur_diff = calc_diff(a, cur_segments)
        if cur_diff > best_diff:
            best_diff = cur_diff
            best_segments = cur_segments
    return best_diff, best_segments

diff, best_segments = solve(a, segments)
print(diff)
print(len(best_segments))
print(' '.join(map(str, [segments.index(s)+1 for s in best_segments])))

