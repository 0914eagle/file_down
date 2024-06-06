
a,b,c=map(int,input().split())
m=int(input())
usb=[]
ps=[]
for i in range(m):
    val,port=input().split()
    if port=="USB":
        usb.append(int(val))
    else:
        ps.append(int(val))
usb.sort()
ps.sort()
ans=0
cost=0
for i in usb:
    if a>0:
        a-=1
        ans+=1
        cost+=i
for i in ps:
    if b>0:
        b-=1
        ans+=1
        cost+=i
for i in ps:
    if c>0:
        c-=1
        ans+=1
        cost+=i
print(ans,cost)
