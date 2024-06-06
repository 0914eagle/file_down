
n = int(input())
a = list(map(int,input().split()))
a.insert(0,0)
dep = [[] for i in range(n+1)]
for i in range(2,n+1):
    x = list(map(int,input().split()))
    for j in range(1,len(x)):
        dep[i].append(x[j])
dp = a.copy()
for i in range(2,n+1):
    if not dep[i]:
        continue
    s = set()
    for j in dep[i]:
        for k in range(1,j):
            if k not in s:
                dp[i] = max(dp[i],dp[j]+dp[k])
                s.add(k)
print(dp[n])
