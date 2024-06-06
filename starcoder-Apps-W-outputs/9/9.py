

n,p=map(int,input().split())
s=0
for i in range(n):
    s+=int(p/2)
    if input()=="halfplus":
        s+=1
print(s)

