
n,a,b,k = map(int,input().split())
s = input()
ans = 0
for i in range(k):
    if s[i] == '+':
        ans += (a**(n-i))*(b**i)
    else:
        ans -= (a**(n-i))*(b**i)
ans = ans%(10**9+9)
print(ans)
