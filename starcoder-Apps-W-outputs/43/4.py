

n=int(input())
l=[]

for i in range(n):
    l.append(list(map(int,input().split())))

l1=[]
l2=[]
for i in l:
    l1.append(i[1])
    l2.append(i[0])
l2.sort()
l3=[]
l4=[]
s=0
for i in range(n):
    s+=l1[i]
    l3.append(s)
    l4.append(l2[i])
max1=max(l3)
max2=l3.index(max1)+1
print(max2,max1)

