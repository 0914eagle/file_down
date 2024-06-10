
N, L = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
for i in range(N):
    a[i] = [a[i], c[i]]

a = sorted(a, key=lambda x: x[1] / x[0])

avg1 = 0
avg2 = 0

for i in range(L):
    avg1 += a[i][0]

avg1 /= L

for i in range(L, N):
    avg2 += a[i][0]

avg2 /= N - L

print(avg1 * avg2)

