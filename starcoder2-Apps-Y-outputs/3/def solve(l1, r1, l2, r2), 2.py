
def solve(l1, r1, l2, r2):
    if l1 == r1:
        return l1, l2
    if l2 == r2:
        return l1, l2
    if l1 < l2:
        return l1, l2
    if l1 > l2:
        return l2, l1

q = int(input())
for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    a, b = solve(l1, r1, l2, r2)
    print(a, b)

