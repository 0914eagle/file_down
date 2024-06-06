
N,X = map(int,input().split())
A = sorted(list(map(int,input().split())))
sum = 0
temp = []
for i in range(len(A)):
  sum += A[i]
  temp.append(sum)
a = []
a.append(0)
b = []
b.append(0)
for i in range(len(temp)):
  b.append(temp[i])
for i in range(1,len(b)):
  a.append(b[i]-b[i-1])

for i in range(len(a)):
  if a[i] > X:
    a.pop(i)
print(len(a))
print(a)
