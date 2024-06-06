
# python 3.6
a,b,l,n = map(int,input().split())
c = []
d = []
for i in range(n):
    c.append(int(input()))
for j in range(l):
    if a in c:
        d.append(a)
    elif a not in c:
        d.append(a)
        a+=b
    else:
        break
if len(d) == l:
    print(len(d))
else:
    print("inf")
