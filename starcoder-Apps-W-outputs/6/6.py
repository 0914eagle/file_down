
n=int(input())
s=0
stack=0
while n>0:
    n-=1
    a=input()
    l=len(a)
    if(a[0]==")" or a[l-1]=="("):
        s+=1
    stack+=a.count("(")
    stack-=a.count(")")
if stack==0:
    print(s)
else:
    print(s+2*stack)
