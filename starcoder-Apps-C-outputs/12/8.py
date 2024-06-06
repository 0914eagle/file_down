
n = int(input())
s = input()
a = []
for _ in range(n):
    a.append(input())
x = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == "R":
            x, y = i, j
b = []
while True:
    b.append((x,y))
    if a[x][y] == "<":
        y-=1
    elif a[x][y] == ">":
        y+=1
    elif a[x][y] == "^":
        x-=1
    elif a[x][y] == "v":
        x+=1
    if (x,y) in b:
        print(len(b) - b.index((x,y)))
        break
