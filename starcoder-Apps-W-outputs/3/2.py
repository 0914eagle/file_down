
# cook your dish here
n,k,q=map(int,input().split())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append([a,b])
m=[]
for i in range(q):
    a,b=map(int,input().split())
    m.append([a,b])
for i in m:
    s=0
    for j in l:
        if i[0]>=j[0] and i[1]<=j[1]:
            s+=1
    if s>=k:
        print(i[1]-i[0]+1)
    else:
        print(0)
