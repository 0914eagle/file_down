
n,k=map(int,input().split())
if k>n:
    print(-1)
else:
    s="abcdefghijklmnopqrstuvwxyz"
    res=''
    if k==1:
        res='a'*(n)
        print(res)
    else:
        res=s[:k]
        res=list(res)
        n-=k
        while(n>0):
            for i in range(k):
                if n>0:
                    res[i]+=s[i]
                    n-=1
                else:
                    break
        print(''.join(res))
