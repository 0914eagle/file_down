
n, m = map(int, input().split())
f = list(map(int, input().split()))
b = list(map(int, input().split()))

m1 = [0]*(n+1)
m2 = [0]*(n+1)
for i in range(n):
    m1[f[i]] = i
    m2[b[i]] = i

for i in range(m):
    if (m1[i+1] != m2[i+1]):
        print('Impossible')
        exit()

for i in range(m):
    print(m1[b[i]] + 1, end = ' ')
