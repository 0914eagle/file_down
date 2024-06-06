
def func(n, f):
    if n == 1:
        return 0
    if n == 2:
        return abs(f[0] - f[1])
    if n == 3:
        return abs(f[0] - f[1]) + abs(f[1] - f[2]) + abs(f[0] - f[2])
    if n == 4:
        return abs(f[0] - f[1]) + abs(f[1] - f[2]) + abs(f[2] - f[3]) + abs(f[3] - f[0])
    if n == 5:
        return abs(f[0] - f[1]) + abs(f[1] - f[2]) + abs(f[2] - f[3]) + abs(f[3] - f[4]) + abs(f[4] - f[0])
    if n == 6:
        return abs(f[0] - f[1]) + abs(f[1] - f[2]) + abs(f[2] - f[3]) + abs(f[3] - f[4]) + abs(f[4] - f[5]) + abs(f[5] - f[0])


n = int(input())
f = list(map(int, input().split()))
print(func(n, f))
