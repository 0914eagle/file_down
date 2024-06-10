

n, k1, k2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

for _ in range(k1):
    a[0] += 1
    a[-1] -= 1
    a.sort()

for _ in range(k2):
    b[0] += 1
    b[-1] -= 1
    b.sort()

error = 0
for i in range(n):
    error += (a[i] - b[i])**2
    
print(error)


