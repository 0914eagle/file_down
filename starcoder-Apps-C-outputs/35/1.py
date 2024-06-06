

from sys import stdin,stdout

read = stdin.readline
write = stdout.write

n, m = map(int, read().split())
arr = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x1,y1,x2,y2 = map(int,read().split())
    arr[x1][y1] += 1
    arr[x1][y2+1] -= 1
    arr[x2+1][y1] -= 1
    arr[x2+1][y2+1] += 1

for i in range(1,n+1):
    for j in range(1,n+1):
        arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]

ans = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        ans += min(i,j)*arr[i][j]

print(ans)


