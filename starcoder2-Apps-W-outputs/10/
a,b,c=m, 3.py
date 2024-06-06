
a,b,c=map(int,input().split())
m=int(input())
usb=[]
ps=[]
for i in range(m):
    val,port=input().split()
    val=int(val)
    if port=='USB':
        usb.append(val)
    else:
        ps.append(val)
usb.sort()
ps.sort()
ans=0
cost=0
i=0
j=0
while i<len(usb) and j<len(ps):
    if usb[i]+ps[j]<1000:
        ans+=1
        cost+=usb[i]+ps[j]
        i+=1
        j+=1
    else:
        break
while i<len(usb) and ans+len(usb)-i<=a+b+c:
    ans+=1
    cost+=usb[i]
    i+=1
while j<len(ps) and ans+len(ps)-j<=a+b+c:
    ans+=1
    cost+=ps[j]
    j+=1
print(ans,cost)
