
a, b, c = map(int, input().split())
m = int(input())
mouses = [(0, 0)] * m
for i in range(m):
    val, port = input().split()
    val = int(val)
    if port == 'USB':
        mouses[i] = (val, 1)
    elif port == 'PS/2':
        mouses[i] = (val, 2)
mouses.sort()
ans = 0
cost = 0
for val, port in mouses:
    if port == 1 and a:
        a -= 1
        ans += 1
        cost += val
    elif port == 2 and b:
        b -= 1
        ans += 1
        cost += val
    elif port == 1 and c:
        c -= 1
        ans += 1
        cost += val
    elif port == 2 and c:
        c -= 1
        ans += 1
        cost += val
print(ans, cost)

