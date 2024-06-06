
n=int(input())
a=input()
z=n+1
r,c=map(int,input().split())
z=n+1
for i in range(n):
  s=input()
  z=n+1
  for j in range(n):
    if s[j]=='R':
      z=0
      r=i
      c=j
#print(r,c)
b=1
while b:
  if a[z%n]=='v':
    if r==n-1:
      print(z%n+1)
      break
    r+=1
    if r==n-1:
      print(z%n+1)
      break
  if a[z%n]=='^':
    if r==0:
      print(z%n+1)
      break
    r-=1
    if r==0:
      print(z%n+1)
      break
  if a[z%n]=='>':
    if c==n-1:
      print(z%n+1)
      break
    c+=1
    if c==n-1:
      print(z%n+1)
      break
  if a[z%n]=='<':
    if c==0:
      print(z%n+1)
      break
    c-=1
    if c==0:
      print(z%n+1)
      break
  z+=1
  if r==n-1 or r==0 or c==n-1 or c==0:
    print(n)
    break
