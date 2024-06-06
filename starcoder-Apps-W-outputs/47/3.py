
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
print(a[-1]*b[-1])
