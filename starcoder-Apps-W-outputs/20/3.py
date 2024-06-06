
n=int(input())
d=list(map(int,input().split()))
a=list(map(int,input().split()))
c=0
for i in range(n):
    if a[i]+d[0]+d[1]<=d[2]:
        c+=1
print(c)
