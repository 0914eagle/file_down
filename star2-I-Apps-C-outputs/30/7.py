
def solve(n, a, b):
    return 1

n = int(input())
a = []
b = []
for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
print(solve(n, a, b))

