
v=int(input())
a=[int(x) for x in input().split()]
if sum(a)<v:
    print(-1)
else:
    ans=''
    for i in range(9,-1,-1):
        cnt=0
        while cnt<v//a[i]:
            cnt+=1
            ans+=str(i)
            v-=a[i]*cnt
        if v==0:
            print(ans)
            break
