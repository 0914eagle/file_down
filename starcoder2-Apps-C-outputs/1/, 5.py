
# 100%

r, c = map(int, input().split())

start = []
target = []
for i in range(r):
    start.append(input())
    target.append(input())

def hammer(i, j):
    start[i] = start[i][:j] + 'X' + start[i][j+1:]
    for k in range(c):
        if start[i][k] == 'O':
            start[i] = start[i][:k] + 'X' + start[i][k+1:]
    for k in range(r):
        if start[k][j] == 'O':
            start[k] = start[k][:j] + 'X' + start[k][j+1:]

for i in range(r):
    for j in range(c):
        if start[i][j] == 'O' and target[i][j] == 'X':
            hammer(i, j)

if start == target:
    print(1)
else:
    print(0)
