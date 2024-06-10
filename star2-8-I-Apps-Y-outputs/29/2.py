
n = int(input())
a = [int(i) for i in input().split()]
a.sort(reverse=True)
res = 0
for i in range(n):
  if a[i] > i+1:
    res += 1
  else:
    break
print(res)

