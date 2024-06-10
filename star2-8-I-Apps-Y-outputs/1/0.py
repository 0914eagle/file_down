
n,k=map(int,input().split())
a=list(map(int,input().split()))
count=0
flag=0
for i in range(1,k+1):
    for j in range(len(a)):
        if(a[j]==i):
            count+=1
    if(count==0):
        flag=1
        break
    count=0
if(flag==1):
    print("NO")
else:
    print("YES")
    for i in range(1,k+1):
        for j in range(len(a)):
            if(a[j]==i):
                print(i,end=" ")

