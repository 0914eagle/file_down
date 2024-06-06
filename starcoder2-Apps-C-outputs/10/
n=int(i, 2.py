
n=int(input())
a=[[0]*n for i in range(n)]
for i in range(n-1):
    b=list(map(int,input().split()))
    for j in range(n-i-1):
        a[i][i+j+1]=b[j]
        a[i+j+1][i]=b[j]
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
