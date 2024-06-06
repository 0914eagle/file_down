
n, s, m, k = map(int,input().split())
a = list(map(int,input().split()))
l = []
for _ in range(s):
  i, j = map(int,input().split())
  l.append([i,j])
flag = 1
for i in l:
  if a[i[0]-1] <= k <= a[i[1]-1]:
    flag = 0
if flag == 0:
  print(k)
else:
  print(-1)
