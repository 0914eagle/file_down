
p,x = map(int,input().split())
n = 10**p
s = 0
for i in range(1,n):
  if ((n//i)*i)%x==0:
    s = i
    break
if s == 0:
  print('Impossible')
else:
  s = (n//s)*s
  print(s)
