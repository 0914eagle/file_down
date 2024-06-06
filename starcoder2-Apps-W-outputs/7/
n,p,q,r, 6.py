
n,p,q,r=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
print(max(p*a[n-1]+q*a[n-1]+r*a[n-1],p*a[n-1]+q*a[n-2]+r*a[n-1],p*a[n-1]+q*a[n-1]+r*a[n-2],p*a[n-1]+q*a[n-2]+r*a[n-2],p*a[n-2]+q*a[n-1]+r*a[n-1],p*a[n-2]+q*a[n-2]+r*a[n-1],p*a[n-2]+q*a[n-1]+r*a[n-2],p*a[n-2]+q*a[n-2]+r*a[n-2]))
