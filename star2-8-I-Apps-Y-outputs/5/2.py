
N,C=map(int,input().split())
W=list(map(int,input().split()))
count=0
s=set()
for w in W:
  if C>=w and w not in s:
    count+=1
    s.add(w)
    C-=w
print(count)

