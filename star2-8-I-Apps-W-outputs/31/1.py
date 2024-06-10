
a,b,c=map(int,input().split())
m=int(input())
val=[]
port=[]
for i in range(m):
    v,p=input().split()
    val.append(int(v))
    port.append(p)
val=sorted(val)
port=sorted(port)
cost=0
i=0
j=0
count=0
while i<m and j<m:
    if port[j]=="USB" and a>0:
        cost+=val[i]
        i+=1
        j+=1
        a-=1
        count+=1
    elif port[j]=="PS/2" and b>0:
        cost+=val[i]
        i+=1
        j+=1
        b-=1
        count+=1
    else:
        j+=1
print(count,cost)

