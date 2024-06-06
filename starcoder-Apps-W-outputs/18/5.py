
n = int(input())
a = []
b = []
for i in range(n):
    a.append([int(x) for x in input().split(' ')])
for i in range(n):
    b.append([int(x) for x in input().split(' ')])

def dfs(x,y):
    if a[x][y] == n:
        return True
    else:
        i,j = a[x][y] - 1, y
        if i == x and j == y:
            return False
        else:
            return dfs(i,j)

if dfs(0,0):
    print('Yes')
else:
    print('No')
