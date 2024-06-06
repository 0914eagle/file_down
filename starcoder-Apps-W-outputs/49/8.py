
# initial and middle part
n=int(input())
for i in range(n):
    l=int(input())
    a=list(map(int,input().split()))
    k=a[0]
    if k==0:
        print('a')
    else:
        print('a'*(k+1))
        for j in range(1,l-1):
            print('a'*(a[j]+1))
        print('a'*(a[l-1]+1))
