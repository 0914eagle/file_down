
n,p,q,r=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=a[-1]*(p+q+r)+a[-2]*q+a[-3]*r
print(ans)
