
n = int(input())
p = input()
m = []
for i in range(n):
    m.append(input())
locx,locy = -1,-1
for i in range(n):
    if 'R' in m[i]:
        locy = i
        locx = m[i].index('R')
        m[i] = m[i].replace('R','.')
        break

def go(x,y,p):
    c = p[0]
    if c == '<':
        nx,ny = x-1,y
        if m[ny][nx] != '.':
            return x,y
    elif c == '>':
        nx,ny = x+1,y
        if m[ny][nx] != '.':
            return x,y
    elif c == '^':
        nx,ny = x,y-1
        if m[ny][nx] != '.':
            return x,y
    elif c == 'v':
        nx,ny = x,y+1
        if m[ny][nx] != '.':
            return x,y
    m[ny][nx] = '#'
    return nx,ny

res = [str(locy+1)+' '+str(locx+1)]

while True:
    for c in p:
        locx,locy = go(locx,locy,p)
        res.append(str(locy+1)+' '+str(locx+1))
        if res[-1] == res[-2]:
            break
    if res[-1] == res[-2]:
        print(len(res)-1)
        break
