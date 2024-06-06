
p,x=map(int,input().split())
num=x
temp=num
if p==1 and x==2:
    print("Impossible")
elif p==1:
    print(x)
else:
    for i in range(p-1):
        temp=temp*10+x
        temp%=pow(10,p)
        if temp==num:
            break
    print(temp)
