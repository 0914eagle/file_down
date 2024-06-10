
def solve(N, x, y, d):
    return 0

N = int(input())
x = [0] * N
y = [0] * N
d = [""] * N
for i in range(N):
    x[i], y[i], d[i] = input().split()
    x[i] = int(x[i])
    y[i] = int(y[i])

print(solve(N, x, y, d))

