
n = int(input())
a = list(map(int, input().split()))
a.sort()

result = 0
for i in range(n-1):
    if a[i] != 0:
        result += a[i]
        a[i+1] += a[i]

if a[n-1] == 0:
    print(-1)
else:
    print(result)

