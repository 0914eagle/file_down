
def solve(l1, r1, l2, r2):
    if l1 == l2:
        return l1, l2 + 1
    if r1 == r2:
        return r1 - 1, r2
    if l1 < l2 and r1 > r2:
        return l1, r2
    if l2 < l1 and r2 > r1:
        return l2, r1
    if l1 < l2 and r1 < r2:
        return l1, r2
    if l2 < l1 and r2 < r1:
        return l2, r1

for _ in range(int(input())):
    l1, r1, l2, r2 = map(int, input().split())
    print(*solve(l1, r1, l2, r2))

