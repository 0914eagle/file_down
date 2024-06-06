
n,x,k=map(int,input().split())
l=list(map(int,input().split()))
a=0
for i in range(n):
    for j in range(i,n):
        if l[i]<=l[j] and l[i]<=k*x<=l[j]:
            a+=1
print(a)
