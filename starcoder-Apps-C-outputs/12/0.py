
n = int(input())
s = input()
a = [list(input()) for _ in range(n)]

def check(sx,sy,d):
    nx,ny = sx,sy
    if d == '<':
        nx -= 1
    elif d == '>':
        nx += 1
    elif d == 'v':
        ny += 1
    else:
        ny -= 1
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        return None
    if a[ny][nx] == '#':
        return None
    return nx,ny

sx,sy = -1,-1
for i in range(n):
    for j in range(n):
        if a[i][j] == 'R':
            sx,sy = j,i
            break

dir = 0
nx,ny = sx,sy
prev = [(sx,sy)]
while True:
    nx,ny = check(nx,ny,s[dir])
    if not nx:
        print(1)
        break
    if (nx,ny) in prev:
        print(len(prev) - prev.index((nx,ny)))
        break
    else:
        prev.append((nx,ny))
    dir = (dir+1)%len(s)
