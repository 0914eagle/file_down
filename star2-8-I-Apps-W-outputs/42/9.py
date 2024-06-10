
import sys
m,d=map(int,input().split())
a=int(input())
b=int(input())
def magic(x,d):
  flag=True
  x=str(x)
  for i in range(len(x)):
    if i%2==0 and int(x[i])==d:
      continue
    elif i%2==0 and int(x[i])!=d:
      flag=False
      break
  return flag
count=0
for i in range(a,b+1):
  if i%m==0 and magic(i,d):
    count+=1
print(count%(10**9+7))

