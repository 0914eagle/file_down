
a=input()
b=int(input())
a=[i for i in a]
k=[]
for i in range(b):
    x=input()
    if len(x)==len(a):
        k.append(x)
c=[]
d=[]
for i in k:
    c.append(i)
while(len(c)>0):
    j=0
    while(j<len(a)):
        for i in c:
            if a[j]==i[j]:
                c.remove(i)
                d.append(i)
                break
        j+=1
if len(d)!=len(a):
    print("impossible")
elif len(d)==len(a) and len(set(d))==1:
    print("ambiguous")
elif len(d)==len(a) and len(set(d))>1:
    print(" ".join(d))

