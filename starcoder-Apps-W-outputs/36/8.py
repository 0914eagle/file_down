

n=int(input())
m=int(input())
a=[]
b=[]
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
c=list(set(a)|set(b))
if(len(c)==n+m):
  print("YES")
else:
  print("NO")
