
def solve(N, x, y, d):
    x_min, x_max = min(x), max(x)
    y_min, y_max = min(y), max(y)
    for t in range(1, 10**9 + 1):
        for i in range(N):
            if d[i] == 'R':
                x[i] += 1
            elif d[i] == 'L':
                x[i] -= 1
            elif d[i] == 'U':
                y[i] += 1
            elif d[i] == 'D':
                y[i] -= 1
        x_min, x_max = min(x), max(x)
        y_min, y_max = min(y), max(y)
        if (x_max - x_min) * (y_max - y_min) == 0:
            return 0
    return (x_max - x_min) * (y_max - y_min)

N = int(input())
x, y, d = [], [], []
for _ in range(N):
    xi, yi, di = input().split()
    x.append(int(xi))
    y.append(int(yi))
    d.append(di)

print(solve(N, x, y, d))

