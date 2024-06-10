
n,c = map(int, input().split())
w = list(map(int, input().split()))
i,j = 0,0
s = 0
while i < n:
  if s+w[i] > c:
    i+=1
  else:
    s += w[i]
    i+=1
    j+=1
print(j)

