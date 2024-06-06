
import bisect

n, g = map(int, input().split())
c_d = []
for _ in range(n):
    d, c = map(int, input().split())
    c_d.append((c, d))
c_d = sorted(c_d)

ans = 0
fuel = 0
for i in range(n):
    c, d = c_d[i]
    idx = bisect.bisect_left(c_d, (c, d-g))
    if idx == len(c_d):
        idx = i
        fuel = g
    else:
        fuel = d - c_d[idx][1]
    ans += c * fuel
print(ans)
