
n,h=map(int,input().split())
a=list(map(int,input().split()))
count=0
for i in range(n):
    if a[i]<=h:
        count=count+1
    else:
        count=count+2
print(count)

