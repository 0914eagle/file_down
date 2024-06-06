
n = int(input())
matrix = [list(input()) for i in range(n)]
x = n
y = n
for i in range(n):
    if matrix[i].count('E')==0:
        x = i
        break
for i in range(n):
    for j in range(n):
        if matrix[j][i]=='E':
            y = i
            break

if x != n and y != n:
    print(x+1,y+1)
else:
    print(-1)
