
n = int(input())
strengths = list(map(int, input().split()))
gcd = 1
for s in strengths:
    gcd = max(gcd, s)
ans = 1
for i in range(len(strengths)):
    if gcd % strengths[i] != 0:
        ans += 1
print(ans)

