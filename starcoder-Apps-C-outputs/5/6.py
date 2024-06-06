
def game(n,a):
    s=0
    for i in range(1,n-1):
        a[i]=max(a[i-1],a[i],a[i+1])-a[i]
    for i in range(1,n-1):
        s=s+max(a[i-1],a[i],a[i+1])-a[i]
    return s
n=int(input())
a=list(map(int,input().split()))
print(game(n,a))
