
n=int(input())
o=[list(map(int,input().split())) for i in range(n)]
p=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        if o[i][j]==0 and p[i][j]!=0:
            print('No')
            exit()
print('Yes')
