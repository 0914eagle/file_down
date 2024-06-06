
import math

def gao(x, y, r):
    ans = 0
    for i in range(n):
        if(x[i]**2 + y[i]**2 >= r[i]**2):
            continue
        if((x[i] == 0 and y[i] == 0) or r[i] == 0):
            continue
        delta = math.sqrt(r[i]**2 - x[i]**2 - y[i]**2)
        a = math.atan2(y[i], x[i])
        b = math.acos(delta / r[i])
        s = a - b
        e = a + b
        if(s < -1e-10):
            ans += 1
        if(e > 1e-10):
            ans += 1
    return ans

n = int(input())
x = [0] * n
y = [0] * n
r = [0] * n
for i in range(n):
    s = input().split()
    x[i] = float(s[0])
    y[i] = float(s[1])
    r[i] = float(s[2])

ans = gao(x, y, r)
x.append(1e-10)
y.append(0)
r.append(1e-10)
ans = max(ans, gao(x, y, r))
print(ans)
