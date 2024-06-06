
n=int(input())
s=input()
res=0
pre=1
for i in range(n-1):
    if s[i]==s[i+1]:
        pre+=1
    else:
        res+=pre
        pre=1
res+=pre
print(res)
