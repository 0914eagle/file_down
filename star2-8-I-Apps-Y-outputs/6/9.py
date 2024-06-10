
n = int(input())
a = list(map(int, input().split()))
s = set()
for i in range(n - 1, -1, -1):
    if a[i] not in s:
        s.add(a[i])
    else:
        a[i] = 0
print(len(s))
print(*a)

