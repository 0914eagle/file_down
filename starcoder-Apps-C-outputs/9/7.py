
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
t=k=0
for i in range(n):
    if a[i]>b[i]:
        a[i]=b[i]
    if a[i]==b[i]:
        t+=a[i]
    else:
        k+=1
        t+=a[i]
print(k,t)
