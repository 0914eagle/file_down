
n=int(input())
m=[[] for i in range(n)]
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(a[0]):
        m[i].append(list(map(int,input().split())))
ans=[]
for i in m[0]:
    if i[1]==0:
        ans.append(i[0])
    else:
        x=m[i[2]][0][0]
        for k in range(1,i[1]):
            x+=m[i[2+k]][0][0]
        ans.append(x+i[0])
print(min(ans))
