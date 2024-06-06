
name=list(map(str,input().split()))
m=min(name[0],name[1])
n=max(name[0],name[1])
if m==name[0]:
    m1=m[:1]
    n1=n[:1]
    print(m1+n1)
else:
    m2=m[:1]
    n2=n[:1]
    print(n2+m2)
