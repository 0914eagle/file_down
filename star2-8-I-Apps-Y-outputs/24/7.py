
X,A,B=map(int,input().split())
if A-B<=X:
  print("delicious")
elif A-B>X+1:
  print("dangerous")
else:
  print("safe")

