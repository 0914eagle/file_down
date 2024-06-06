
n=int(input())
m=list(map(int,input().split()))

v=""
for i in range(len(m)):
    if n>=m[i]:
        v+=str(i+1)
        n-=m[i]
if v=="":
    v+=-1
print(v)

