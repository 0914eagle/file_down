
n,m,k=map(int,input().split())
ans=0
for i in range(k):
    ans+=n+m-2-i
    print('(1,1)',end=' ')
    for j in range(i):
        print('(%d,%d)'%(1,j+2),end=' ')
    for j in range(n-1):
        print('(%d,%d)'%(j+2,i+2),end=' ')
    print()
print(ans)
