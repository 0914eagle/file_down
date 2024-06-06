
a=list(map(int,input().split()))
s=sum(a)
flag=0
for i in range(len(a)):
    if 2*a[i]==s-a[i]:
        flag=1
if flag==1:
    print("Yes")
else:
    print("No")
