
n,p,q,r=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
print(max(p*a[n-1]+q*a[n-1]+r*a[n-1],p*a[0]+q*a[0]+r*a[n-1],p*a[0]+q*a[n-1]+r*a[n-1],p*a[0]+q*a[0]+r*a[0]))
