
def check(s,k):
    l,r=0,0
    for i in s:
        if i=='(':
            l+=1
        else:
            r+=1
        if r>l:
            return False
    if r==l:
        return True
    else:
        return False

def solve(s,v,k,l,r,d):
    if k==0:
        return 0
    if (l,r,d) in dp:
        return dp[(l,r,d)]
    res=-inf
    if l>0:
        res=max(res,solve(s,v,k-1,l-1,r,1)+v[0])
    if r>0:
        res=max(res,solve(s,v,k-1,l,r-1,-1)+v[-1])
    if d==-1:
        if l>0:
            res=max(res,solve(s[1:],v[1:],k-1,l-1,r,1)+v[0])
    elif d==1:
        if r>0:
            res=max(res,solve(s[:-1],v[:-1],k-1,l,r-1,-1)+v[-1])
    dp[(l,r,d)]=res
    return res

n,k=map(int,input().split())
s=input()
l=r=0
for i in s:
    if i=='(':
        l+=1
    else:
        r+=1
if not check(s,k):
    print('?')
else:
    v=list(map(int,input().split()))
    dp={}
    print(solve(s,v,k,l,r,0))
