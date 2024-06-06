
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n):
    if a[i] >= 0:
        ans = i+1
print(ans)
