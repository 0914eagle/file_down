
n,k = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
if k>n:
    print("NO")
else:
    print("YES")
    s = [0]*n
    t = list(range(k))
    for i in range(n):
        s[p[i]-1] = t[q[i]-1]
        t.sort()
    print("".join(map(chr,s)))

