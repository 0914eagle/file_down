
b1,q,l,m=map(int,input().split())
s=0
if(b1==q==0):
    print(0)
elif(b1==q):
    a=list(map(int,input().split()))
    if(b1 in a):
        print(0)
    else:
        print(1)
else:
    s=0
    a=list(map(int,input().split()))
    flag=0
    if(b1==0):
        if(q==0):
            s=l+1
        else:
            s=l//abs(q)+1
        if(0 in a):
            s-=1
        print(s)
    else:
        for i in range(1,l+1):
            if(abs(b1)>l):
                break
            if(b1 in a):
                flag=1
                break
            s+=1
            b1=b1*q
        if(flag==1):
            print(0)
        else:
            print(s)
