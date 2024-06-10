
n, m = map(int, input().split())
a = [0] * (n + 1)
b = [0] * (n + 1)
for i in range(m):
    x, y = map(int, input().split())
    a[x] += 1
    b[y] += 1
for x in range(1, n + 1):
    for y in range(x + 1, n + 1):
        if a[x] > 0 and b[y] > 0 or a[y] > 0 and b[x] > 0:
            print("YES")
            exit()
print("NO")

