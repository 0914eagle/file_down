
n, m = map(int, input().split())
a = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

def solve(a, segments):
    min_val = min(a)
    max_val = max(a)
    diff = max_val - min_val
    for l, r in segments:
        min_val_after = min(min_val - 1, a[l - 1], a[r - 1])
        max_val_after = max(max_val - 1, a[l - 1], a[r - 1])
        diff_after = max_val_after - min_val_after
        if diff_after > diff:
            diff = diff_after
            min_val = min_val_after
            max_val = max_val_after
    return diff

print(solve(a, segments))

