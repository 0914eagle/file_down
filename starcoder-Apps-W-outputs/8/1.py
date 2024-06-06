
a = list(map(int, input().split()))
m = a[1]
k = a[2]
n = a[0]
b = list(map(int, input().split()))
b.sort(reverse=True)
s = 0
for i in range(k):
  s = s + sum(b[i*m:m*(i+1)])
print(s)
print(m-1)
