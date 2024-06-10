
n, k = list(map(int, input().split()))
p = list(map(int, input().split()))
q = list(map(int, input().split()))

def f(n, k):
  s = [chr(ord('a') + i) for i in range(k)]
  for i in range(1, n):
    if p[i - 1] > p[i]:
      s[q[i - 1] - 1], s[q[i] - 1] = s[q[i] - 1], s[q[i - 1] - 1]
  return ''.join(s)

print("YES")
print(f(n, k))

