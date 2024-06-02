
def solve(l1, r1, l2, r2):
    if l1 > l2:
        l1, r1, l2, r2 = l2, r2, l1, r1
    if r1 < r2:
        return r1, r2
    return r1, l2

q = int(input())
for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    print(*solve(l1, r1, l2, r2))

