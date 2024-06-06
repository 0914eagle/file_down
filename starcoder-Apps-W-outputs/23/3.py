
n,m=map(int,input().split())
adj=[[]for _ in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

for i in range(n):
    if len(adj[i])>2:
        ans=[i]
        for j in adj[i]:
            if j not in ans:
                ans.append(j)
        ans=ans+[i]
        print(2)
        print(len(ans))
        for x in ans:
            print(x+1,end=' ')
        print()
        break
else:
    ans=[]
    for i in range(n):
        if len(adj[i])==1 and ans==[]:
            ans=[i]
        elif len(adj[i])==1 and ans!=[]:
            ans.append(i)
    if len(ans)>=3:
        ans=ans+[ans[0]]
        print(2)
        print(len(ans))
        for x in ans:
            print(x+1,end=' ')
        print()
    else:
        print(1)
        print(n)
        for i in range(n):
            print(i+1,end=' ')
        print()
