
num=[int(i) for i in input().split()]
num.sort()
x=sum(num[0:3])
y=sum(num[3:])
if(x==y):
  print("YES")
else:
  print("NO")
