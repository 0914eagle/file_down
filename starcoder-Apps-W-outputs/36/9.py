

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)

n, m = map(int, input().split())

if n > m:
    m, n = n, m

x = []
y = []

for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

for i in range(m):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

res = "NO"

for i in range(n):
    for j in range(m):
        r = distance(x[i], y[i], x[n+j], y[n+j])
        flag = True
        for k in range(n):
            if distance(x[i], y[i], x[k], y[k]) > r:
                flag = False
                break
        if flag:
            for k in range(m):
                if distance(x[i], y[i], x[n+k], y[n+k]) < r:
                    flag = False
                    break
        if flag:
            res = "YES"
            break
print(res)

