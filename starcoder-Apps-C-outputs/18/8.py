
def solve():
    n, k = map(int,input().split())
    c = list(map(int,input().split()))
    ans = []
    for i in range(1<<n):
        s = 0
        for j in range(n):
            if(i&(1<<j)):
                s += c[j]
        if(s <= k):
            ans.append(s)
    ans.sort()
    q = len(ans)
    print(q)
    print(*ans)
    
t = 1
while(t>0):
    solve()
    t -= 1
