
a, b, c = map(int, input().split())
m = int(input())
mouses = [[0, 0] for i in range(m)]
for i in range(m):
    val, port = input().split()
    mouses[i][0] = val
    mouses[i][1] = port
mouses = sorted(mouses, key=lambda x: x[0])
num_comp = 0
total_cost = 0
for i in range(m):
    if mouses[i][1] == "USB" and a > 0:
        a -= 1
        num_comp += 1
        total_cost += int(mouses[i][0])
    elif mouses[i][1] == "PS/2" and b > 0:
        b -= 1
        num_comp += 1
        total_cost += int(mouses[i][0])
    elif mouses[i][1] == "PS/2" and a > 0 and c > 0:
        a -= 1
        c -= 1
        num_comp += 1
        total_cost += int(mouses[i][0])
print(num_comp, total_cost)

