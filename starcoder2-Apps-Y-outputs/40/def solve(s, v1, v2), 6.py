
def solve(s, v1, v2):
    if s % (v1 - v2) != 0:
        return "Impossible"
    else:
        return s // v1, s // v2

s, v1, v2 = map(int, input().split())
print(*solve(s, v1, v2))

