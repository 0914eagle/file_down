
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

def solve(a, k):
    if k == 1:
        return len(a)
    if len(a) == 1:
        return 0
    if len(a) == 2:
        if abs(a[0] - a[1]) <= 5:
            return 2
        else:
            return 1
    if abs(a[0] - a[1]) <= 5:
        return solve(a[2:], k - 1) + 2
    else:
        return solve(a[1:], k)

print(solve(a, k))

