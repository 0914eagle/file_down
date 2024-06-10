
h=list(map(int,input().split()))[1:]
b=list(map(int,input().split()))[1:]
def gcd(a,b):
  if b==0:
    return a
  return gcd(b,a%b)
def lcm(a,b):
  return a*b/gcd(a,b)
def hdb(h,b):
  l=1
  for i in h:
    l=lcm(l,i)
  for j in b:
    l=lcm(l,j)
  x=0
  y=0
  for i in h:
    x+=l/i
  for j in b:
    y+=l/j
  if x==y:
    return int(x)
  else:
    return "impossible"
print(hdb(h,b))

