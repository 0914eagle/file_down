
def sol(n,m,k):
    m=min(n,m)
    if(k<=m):
        return k
    else:
        return ((k-m-1)//(m-1)*(m-1)+m)
n,m,k=map(int,input().split())
print(sol(n,m,k))
