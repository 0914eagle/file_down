
def solve(n, p):
    x = 0
    for i in range(n):
        x += p[i] ** (i + 1)
    return x

n = int(input())
p = []
for _ in range(n):
    p.append(int(input()))
print(solve(n, p))

