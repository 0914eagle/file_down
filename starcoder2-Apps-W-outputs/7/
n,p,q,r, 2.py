
n,p,q,r=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
print(max(p*a[-1]+q*a[-1]+r*a[-1],p*a[-1]+q*a[-1]+r*a[0],p*a[-1]+q*a[0]+r*a[0],p*a[0]+q*a[0]+r*a[0]))
