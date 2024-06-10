
n = int(input())
a = list(map(int, input().split()))

idx = {}
res = []
for i, num in enumerate(a):
  if num not in idx:
    idx[num] = i
  else:
    res.append(idx[num])
    idx[num] = i
    
print(n - len(res))
print(*a)

