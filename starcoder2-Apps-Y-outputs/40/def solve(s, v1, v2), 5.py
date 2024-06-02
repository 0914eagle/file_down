
def solve(s, v1, v2):
    if s == 0:
        return 0, 0
    if s % v2 == 0:
        return 0, s // v2
    if s % v1 == 0:
        return s // v1, 0
    if s % v1 < v2:
        return 0, s // v2
    if s % v1 > v2:
        return s // v1, 0
    return 0, 0

s, v1, v2 = map(int, input().split())
if v1 < v2:
    v1, v2 = v2, v1

if v1 > s:
    print("Impossible")
else:
    print(*solve(s, v1, v2))

