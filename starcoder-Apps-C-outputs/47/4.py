
n, k = map(int, input().split())
res = []
for i in range(k-1):
    res.append("a")
    n -= 1
for j in range(n):
    res.append("z")
print("".join(res))
