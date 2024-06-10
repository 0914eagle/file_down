
n, k = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

if n < k:
  print("NO")
  exit()

s = [None] * n
s[p[0] - 1] = chr(ord('a') + k - 1)

for i in range(1, n):
  idx = p[i] - 1
  s[idx] = chr(ord(s[idx - 1]) + 1)
  if ord(s[idx]) - ord('a') >= k:
    print("NO")
    exit()

s = [None] * n
s[q[0] - 1] = chr(ord('a') + k - 1)

for i in range(1, n):
  idx = q[i] - 1
  s[idx] = chr(ord(s[idx - 1]) + 1)
  if ord(s[idx]) - ord('a') >= k:
    print("NO")
    exit()

print("YES")
print("".join(s))

