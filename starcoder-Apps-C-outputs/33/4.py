
a,b,l,r=map(int,input().split())
if l==r:
    print(1)
elif l<=b+1<=r:
    print(a)
elif l==1 and b>=r:
    print(a)
else:
    print(a-1)
