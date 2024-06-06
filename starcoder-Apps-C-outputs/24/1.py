
# cook your dish here
n = int(input())
mat = []
for i in range(n):
    mat.append(input())

ans = []

for i in range(n):
    for j in range(n):
        if mat[i][j] == '.':
            ans.append([i+1, j+1])

for i in ans:
    print(i[0], i[1])
