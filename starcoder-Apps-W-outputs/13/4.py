
n,x,k=list(map(int,input().split()))
a=list(map(int,input().split()))
print((n-a.index(min(a,key=lambda x:x%x<1)))*(n-a[::-1].index(min(a[::-1],key=lambda x:x%x<1))))
