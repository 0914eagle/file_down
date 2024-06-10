
n = int(input())
x = list(map(int, input().split()))
x.sort()
p = x[n//2]
ans = 0
for i in range(n):
    ans += (x[i] - p)**2
print(ans)

