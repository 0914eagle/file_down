
def error(a, b):
  err = 0
  for i in range(len(a)):
    err += (a[i] - b[i])**2
  return err
  
n, k1, k2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
for i in range(k1):
  if a[0] < b[0]:
    a[0] += 1
  else:
    a[0] -= 1
for i in range(k2):
  if b[0] < a[0]:
    b[0] += 1
  else:
    b[0] -= 1
print(error(a, b))

