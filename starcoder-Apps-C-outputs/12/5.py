
def f(x,y,s):
    if x == 0 or y == 0 or x == n or y == n:
        return
    if g[x][y] != '.':
        return
    g[x][y] = '#'
    if s == '<':
        f(x,y-1,s)
    if s == '>':
        f(x,y+1,s)
    if s == '^':
        f(x-1,y,s)
    if s == 'v':
        f(x+1,y,s)

n = int(input())
a = input()
g = []
for i in range(n):
    g.append(list(input()))
x = 0
y = 0
for i in range(n):
    for j in range(n):
        if g[i][j] == 'R':
            x = i
            y = j
f(x,y,a[0])
a = a[1:]
a = a + a
b = len(a)
ans = b
for i in range(b):
    if a[i] == '<':
        if y == 0:
            continue
        else:
            y -= 1
    if a[i] == '>':
        if y == n - 1:
            continue
        else:
            y += 1
    if a[i] == 'v':
        if x == n - 1:
            continue
        else:
            x += 1
    if a[i] == '^':
        if x == 0:
            continue
        else:
            x -= 1
    if g[x][y] == '#':
        ans = i + 1
        break
print(ans)
