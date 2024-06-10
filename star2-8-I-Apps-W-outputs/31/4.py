
a, b, c = map(int, input().split())
m = int(input())
mouses = []
for i in range(m):
    val, typ = input().split()
    val = int(val)
    mouses.append((val, typ))

mouses.sort()
count = 0
cost = 0
for val, typ in mouses:
    if typ == "USB" and a > 0:
        count += 1
        cost += val
        a -= 1
    elif typ == "PS/2" and b > 0:
        count += 1
        cost += val
        b -= 1
    elif c > 0:
        count += 1
        cost += val
        c -= 1
    if count == a + b + c:
        break

print(count, cost)

