
from collections import Counter

N = int(input())

cx, cy, r = [], [], []
for _ in range(N):
    x, y, rr = map(int, input().split())
    cx.append(x)
    cy.append(y)
    r.append(rr)

def at_point(x, y):
    cnt = 0
    for i in range(N):
        if (cx[i] - x)**2 + (cy[i] - y)**2 < r[i]**2:
            cnt += 1
    return cnt

def check(x, y):
    cnt = 0
    for i in range(N):
        if (cx[i] - x)**2 + (cy[i] - y)**2 < r[i]**2:
            cnt += 1
    return cnt

def solve():
    ans = 0
    for x in range(-1000, 1001):
        for y in range(-1000, 1001):
            ans = max(ans, check(x, y))
    print(ans)

solve()
