
n,p = map(int,input().split())
a = [0]*n
for i in range(n):
  a[i] = input()
t = p//2
s = 0
for i in range(n):
  if a[i] == "halfplus":
    s += t
  s += t
print(s)
