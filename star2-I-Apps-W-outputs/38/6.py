
def solve(N, x, y, d):
    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    y_max = max(y)
    for i in range(N):
        if d[i] == "R":
            x_min = max(x_min, x[i])
        elif d[i] == "L":
            x_max = min(x_max, x[i])
        elif d[i] == "U":
            y_min = max(y_min, y[i])
        elif d[i] == "D":
            y_max = min(y_max, y[i])
    return (x_max - x_min) * (y_max - y_min)

N = int(input())
x = [0] * N
y = [0] * N
d = [""] * N
for i in range(N):
    x[i], y[i], d[i] = input().split()
    x[i] = int(x[i])
    y[i] = int(y[i])
print(solve(N, x, y, d))

