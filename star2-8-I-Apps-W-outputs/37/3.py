
n, h = list(map(int, input().split()))
a = list(map(int, input().split()))
bent = 0
normal = 0
for i in range(n):
  if a[i] > h:
    bent += 1
  else:
    normal += 1
print(bent*2 + normal)

