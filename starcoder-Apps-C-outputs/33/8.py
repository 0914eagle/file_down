
a,b,l,r=map(int,input().split())

if a<b:
    if r<=a:
        print(r)
    elif l>a:
        print(a)
    else:
        print(a)
else:
    if r<=a:
        print(r)
    elif l<=a:
        print(l)
    else:
        print(a)
