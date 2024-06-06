
from sys import stdin

n=int(input())
program=input()
grid=[]
for i in range(n):
    grid.append(input())

for i in range(n):
    if 'R' in grid[i]:
        sx,sy=i,grid[i].index('R')
        break

vis=[[False]*n for _ in range(n)]

def find_next(x,y,ch):
    if ch=='<':
        x,y=x,y-1
    elif ch=='>':
        x,y=x,y+1
    elif ch=='^':
        x,y=x-1,y
    else:
        x,y=x+1,y
    if 0<=x<n and 0<=y<n and grid[x][y]!='#':
        return (x,y)
    else:
        return (x,y)

def check(x,y,ch):
    if ch=='<':
        x,y=x,y-1
    elif ch=='>':
        x,y=x,y+1
    elif ch=='^':
        x,y=x-1,y
    else:
        x,y=x+1,y
    if 0<=x<n and 0<=y<n and grid[x][y]!='#':
        return True
    else:
        return False

def dfs(x,y,ch,flag):
    global length,ans
    vis[x][y]=True
    if vis[sx][sy]:
        length+=1
        ans=(length,flag)
        return 
    if check(x,y,ch):
        x,y=find_next(x,y,ch)
    else:
        flag+=1
    dfs(x,y,program[flag%len(program)],flag)

ans=(0,0)
length=0
dfs(sx,sy,program[0],0)

if ans[0]==0:
    print(1)
else:
    print(ans[0])
