
n=int(input())
a=list(map(int,input().split()))
if sum(a)%2!=0:
    print('NO')
else:
    print('YES',max(a))
    for i in range(1,n):
        if a[i]>=1:
            print(1,i+1)
            a[i]-=1
        if a[0]>=1:
            print(i+1,1)
            a[0]-=1
    for i in range(1,n):
        if a[0]>0:
            print(1,i+1)
            a[0]-=1
        if a[i]>0:
            print(i+1,1)
            a[i]-=1
