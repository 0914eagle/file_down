
n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

a = [i for i in a if (i-1) % 2 == 0]
b = [i for i in b if i % 2 == 1]
a.sort()
b.sort()
ans = 0
i = 0
for j in b:
  while i < len(a) and a[i] < j:
    i += 1
  if i < len(a):
    ans += 1
    i += 1

print(ans)

