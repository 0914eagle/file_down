
n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()
print(a[0]*b[-1])
