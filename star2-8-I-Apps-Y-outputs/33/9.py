
n, d = map(int, input().split())
is_gold = [False] * n
is_gold[n//2] = True
res = 0
for i in range(n):
  if is_gold[i]:
    res += 1
    for j in range(max(0, i-d), min(n, i+d+1)):
      is_gold[j] = True
print(res)

