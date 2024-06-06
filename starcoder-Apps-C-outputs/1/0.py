
s=input().split()
a=int(s[0])
b=int(s[1])
l=[]
for i in range(a,b+1):
    c=str(i)
    while len(c)>1:
        p=1
        for j in c:
            p=p*int(j)
        c=str(p)
    l.append(c)
for i in range(1,10):
    print(l.count(str(i)),end=" ")

