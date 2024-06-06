
n=int(input())
s=input()
res=0
cnt=0
for i in range(n-1,-1,-1):
    if s[i]!=s[i-1]:
        cnt+=1
    else:
        res=max(res,cnt)
        cnt=0
print(res+n)
