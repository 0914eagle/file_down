
def f(n,r,p):
    if n==1:return 0
    if r<=p:return 0
    if p==0:return 10**9
    a=f((n+1)//2,r,p)+1+f(n//2,r,p)
    b=f((n+1)//2,r,p)+1+f((n+1)//2,r-p,p)+1+f(n//2,r-p,p)
    return min(a,b)

n,r,p=map(int,input().split())
print(f(n,r,p))
