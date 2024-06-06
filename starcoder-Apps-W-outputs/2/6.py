
n,h,m,k=map(int,input().split())
h_i=[0]*n
m_i=[0]*n
for i in range(n):
    h_i[i],m_i[i]=map(int,input().split())

li=[]
for i in range(0,m//2):
    cnt=0
    for j in range(n):
        if((i+m_i[j])%m)<=k:
            cnt+=1
    li.append(cnt)
li=list(enumerate(li))
li.sort(key=lambda x:x[1])

print(li[0][1],0)
print(" ".join([str(i+1) for i in range(n) if (li[0][0]+m_i[i])%m>k]))
