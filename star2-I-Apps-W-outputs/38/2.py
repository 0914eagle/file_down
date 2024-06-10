
def solve(N, x, y, d):
    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    y_max = max(y)
    if 'L' in d:
        x_min = -10**8
    if 'R' in d:
        x_max = 10**8
    if 'D' in d:
        y_min = -10**8
    if 'U' in d:
        y_max = 10**8
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

