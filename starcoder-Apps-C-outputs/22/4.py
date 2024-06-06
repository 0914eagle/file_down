

n,m,h = map(int,input().split())
x = list(map(int,input().split()))
for _ in range(m):
    c1,c2 = map(int,input().split())
ans = []
s = set()
for i in range(h):
    for j in range(n):
        if x[j] == i:
            s.add(j)
    if len(s) > 1:
        ans.append(j)
        s = set()
        s.add(j)
print(len(ans))
for i in ans:
    print(i+1,end = " ")
