
n = int(input())
a = list(map(int, input().split()))

if max(a) == 0:
  print(-1)
  exit()
m = max(a)

def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

for i in range(n):
  if a[i] != 0:
    m = gcd(m, a[i])
    
print(m * n - sum(a))


